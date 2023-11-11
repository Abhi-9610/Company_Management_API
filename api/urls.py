from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewset,employeeviewset

# Create a router and register your viewset
router = DefaultRouter()
router.register(r'companies', CompanyViewset)
router.register(r'employee', employeeviewset)

urlpatterns = [
    path('', include(router.urls)),
]
