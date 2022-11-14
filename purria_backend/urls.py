from rest_framework.routers import DefaultRouter
from purria_backend.views import ContractModelViewSet,GardenModelView
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register(r'contracts',ContractModelViewSet,basename='contract'),
router.register(r'gardens', GardenModelView, basename='garden')

urlpatterns = [
    path("",include(router.urls))
]
    
