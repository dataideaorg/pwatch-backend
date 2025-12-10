from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillViewSet, BillReadingViewSet

router = DefaultRouter()
router.register(r'bills', BillViewSet, basename='bill')
router.register(r'readings', BillReadingViewSet, basename='reading')

urlpatterns = [
    path('', include(router.urls)),
]