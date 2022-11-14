from wsgiref import validate
from .models import CustomUser
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class SignUpSerializer(serializers.ModelSerializer):
    
    email = serializers.CharField(max_length=30,required=True)
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(min_length=8, write_only=True)#keeping the pass protected

    class Meta:
        model = CustomUser
        fields = ['email','username','password']

    def validate(self, attrs):
        
        email_exists = CustomUser.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError('email address already been used!')
        
        return super().validate(attrs)
        
        
    #create is called when we use .save() on our serializer class instance
    def create(self, validated_data):
        
        password = validated_data.pop("password")
        
        user = super().create(validated_data)
        
        user.set_password(password)
        
        user.save()
        
        Token.objects.create(user=user)
        
        return user