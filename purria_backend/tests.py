from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from purria_backend.views import ContractListCreateView
from django.contrib.auth import get_user_model
from rest_framework import status
from model_bakery import baker
from purria_backend.models import Contract,Garden
from Accounts.models import CustomUser
from django.core.exceptions import ValidationError
from purria_backend.serializers import ContractSerializer

User = get_user_model()

# Create your tests here.
class ContractListCreateTest(TestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ContractListCreateView().as_view()
        self.url = 'contract_list_create'
        self.user = CustomUser.objects.create(
            username="testcase",
            email="test@case.com",
        )
        
    def test_anonymous_user(self):
        
        request = self.factory.get(self.url)
        response = self.view(request)      
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        
    def test_create_default_contract(self):
        
        garden = baker.prepare(Garden, _quantity=10)
        baker.make(Contract, level =1, garden=garden,user=self.user)
            
        request = self.factory.get(self.url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        breakpoint()
        
        self.assertEqual(1, response.data['result'][0]['level'])
        self.assertEqual(1, Contract.objects.count())
        self.assertEqual(self.user.email, response.data['result'][0]['user'])
        self.assertEqual(10, len(response.data['result'][0]['garden']))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
    

    