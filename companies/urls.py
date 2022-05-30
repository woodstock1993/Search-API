from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'tag', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]
