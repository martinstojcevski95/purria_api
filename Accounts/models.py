from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel
from .manager import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin,TimeStampedModel):
    
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=30, null=True)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects  = CustomUserManager()
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:    
        ordering = ['-date_joined']
        
