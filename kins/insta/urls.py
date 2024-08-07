from django.urls import path
from .views import signup ,verify_email , login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('verify/<str:token>/', verify_email, name='verify_email'), # Email verification URL moklse
    path('login/', login, name='login')
]
