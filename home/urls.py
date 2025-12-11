from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroImageViewSet, HeadlineViewSet

router = DefaultRouter()
router.register(r'hero-images', HeroImageViewSet, basename='hero-image')
router.register(r'headlines', HeadlineViewSet, basename='headline')

urlpatterns = [
    path('', include(router.urls)),
]

