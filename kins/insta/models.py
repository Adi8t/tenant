# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True

class Domain(DomainMixin):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)   #ek j user link hase userprofile thi...  
    tenant = models.ForeignKey(Client, on_delete = models.CASCADE)
    verification_token =  models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username



