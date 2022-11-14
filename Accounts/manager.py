from multiprocessing.sharedctypes import Value
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    
    #custom user model manager where email is the unique identifier for authentication
    def create_user(self, email, password, **extra_fields):
        
        if email is None:
            raise ValueError(_('the email must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    
    #create and save superuser with the given email and password
    def create_superuser(self, email, password, **extra_fields):
        
       is_staff = extra_fields.setdefault('is_staff',True)
       extra_fields.setdefault('is_active',True)
       is_superuser = extra_fields.setdefault('is_superuser',True)
       
       if is_staff is not True:
           raise ValueError(_('Super user  is_staff must be set to true'))
       if is_superuser is not True:
           raise ValueError(_('SuperUser is_superuser must be set to true'))
       
       return self.create_user(email, password, **extra_fields)
   

            
    
        