from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, HomeBlogSummaryView

router = DefaultRouter()
router.register(r'', BlogViewSet, basename='blog')

urlpatterns = [
    path('home-summary/', HomeBlogSummaryView.as_view(), name='home-blog-summary'),
    path('', include(router.urls)),
]

