from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Client
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
from insta.serializer import Userprofileserializer
import uuid
from django_tenants.utils import schema_context

@api_view(['POST'])
def signup(request):
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')
    tenant_id = request.data.get('tenant_id')

    if User.objects.filter(email=email).exists():
        return Response({'message': 'Email already exists.'})

    user = User.objects.create(email=email, username=username )
    user.is_active=False
    user.set_password(password)  
    user.save()
    
    try:
        tenant = Client.objects.get(id = tenant_id)
    except Client.DoesNotExist:
        return Response({'message': 'Tenant ID not found.'})

    profile = UserProfile.objects.create(user=user, tenant = tenant)

    token = str(uuid.uuid4())
    profile.verification_token = token
    profile.save()  
    subject = 'Verify your email'
    message = f'Click the link to verify your email: http://localhost:8000/api/verify/{token}/'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
    return Response({'message': 'User created. Please check your email for verification.'})

@api_view(['GET'])
def verify_email(request, token):
    try:
        profile = UserProfile.objects.get(verification_token = token)
        user = profile.user
        user.is_active = True           # apda jode frontend nahi etla khli url ne browser ma hit karvani 
        user.save()                     # user valid thay token thi toj active thay 
        return Response("Email verified successfully.")
    except UserProfile.DoesNotExist:
        return Response("Invalid token.")

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    print(username)
    password = request.data.get('password')
    print(password)
    tenant_id = request.data.get('tenant_id')
    print(tenant_id)

    user = authenticate(username = username , password = password)
    if user is None:
        return Response("Invalid username or password.")

    try:
        profile = UserProfile.objects.get(user = user, tenant = tenant_id)
        print(profile)
        print(profile.tenant)
    except UserProfile.DoesNotExist:
        return Response("User not assigned  this tenant.")

    serializer = Userprofileserializer(profile)
    return Response({
        'message': "Login successful",
        'data': serializer.data
    })
