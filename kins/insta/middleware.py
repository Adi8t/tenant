# insta/middleware.py
from urllib import response
from django.db import connection
from django.utils.deprecation import MiddlewareMixin
from .models import UserProfile
from django_tenants.utils import get_tenant_model

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user = request.user)
                tenant = user_profile.tenant
                connection.set_tenant(tenant)
            except UserProfile.DoesNotExist:
                pass