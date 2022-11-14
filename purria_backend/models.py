from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from django.contrib.auth import get_user_model
from Accounts.models import CustomUser
from django.core.exceptions import ValidationError

User = get_user_model()

class Garden(models.Model):
    
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
    
# Create your models here.
class Contract(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True, editable=False)
    name = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=200, default="")
    level = models.IntegerField( default=1, blank=False, validators = [
        MaxValueValidator(3),
        MinValueValidator(1)
    ])
    garden = models.ManyToManyField(Garden, related_name="garden")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='contract_user', null=True)
    
        
    def __str__(self):
        return self.name