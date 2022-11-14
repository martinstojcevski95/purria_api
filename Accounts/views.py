from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user



# Create your views here.
class SignUpView(generics.GenericAPIView):
    
    permission_classes = []
    
    serializer_class = SignUpSerializer
    
    #@swagger_auto_schema(operation_description="Signs in the user")
    def post(self, request : Request):
        
        data = request.data
        
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            
            response = {
                'message' : 'user created successfully',
                'response' : serializer.data
            }
            
            return  Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoginView(APIView):
    
    
    permission_classes = []
    
    #@swagger_auto_schema(operation_description="Login in the user")
    def post(self, request : Request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            
            
            tokens = create_jwt_pair_for_user(user)
            
            response = {
                'message': 'login successfull',
                'tokens' : tokens
            }
            
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
   # @swagger_auto_schema(operation_description="Shows the request info")
    def get(self, request : Request):
        
        response = {
            'user' : str(request.user),
            'auth' : str(request.auth)         
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    