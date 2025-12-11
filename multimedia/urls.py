from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import XSpaceViewSet, PodcastViewSet, GalleryViewSet

router = DefaultRouter()
router.register(r'x-spaces', XSpaceViewSet, basename='xspace')
router.register(r'podcasts', PodcastViewSet, basename='podcast')
router.register(r'gallery', GalleryViewSet, basename='gallery')

urlpatterns = [
    path('', include(router.urls)),
]

