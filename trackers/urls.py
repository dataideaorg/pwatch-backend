from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillViewSet, BillReadingViewSet, MPViewSet, DebtDataViewSet

router = DefaultRouter()
router.register(r'bills', BillViewSet, basename='bill')
router.register(r'readings', BillReadingViewSet, basename='reading')
router.register(r'mps', MPViewSet, basename='mp')
router.register(r'debt', DebtDataViewSet, basename='debt')

urlpatterns = [
    path('', include(router.urls)),
]