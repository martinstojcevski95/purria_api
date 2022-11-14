from rest_framework.routers import DefaultRouter
from purria_backend.views import ContractListCreateView
from django.urls import path
from . import views

urlpatterns = [
    
    path('contracts/', views.ContractListCreateView.as_view(), name='contract_list_create'),   
]
    
