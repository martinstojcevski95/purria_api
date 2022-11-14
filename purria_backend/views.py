from rest_framework import viewsets
from purria_backend.serializers import ContractSerializer,GardenSerializer
from purria_backend.models import Contract,Garden
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from rest_framework import generics,status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.

class ContractListCreateView(generics.ListCreateAPIView
):

    """ a view for creating and listing contractss """
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated] 
    queryset = Contract.objects.all()
    
    def get_queryset(self):
        #if user.is_anonymous is None:
        return Contract.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        user = self.request.user
        contract =serializer.save(user=user)
        for i in range(contract.level * 10):
            newgarden = Garden.objects.create(garden_contract_id=contract.id)
            contract.garden.add(newgarden) 
        return super().perform_create(serializer)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(data={'result':serializer.data}, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        
class GardenModelView(viewsets.ModelViewSet):
    
    http_method_names = ['get','post','delete','put']
    queryset = Garden.objects.all()
    serializer_class = GardenSerializer
    permission_classes = []
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)