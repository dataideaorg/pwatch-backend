from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import XSpace, Podcast, Gallery
from .serializers import XSpaceSerializer, PodcastSerializer, GallerySerializer


class XSpacePagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class XSpaceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for X Spaces events
    
    Provides list, retrieve, create, update, and destroy actions
    Filters by status and scheduled_date
    Search by title, description, host, and topics
    """
    queryset = XSpace.objects.all()
    serializer_class = XSpaceSerializer
    pagination_class = XSpacePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['title', 'description', 'host', 'topics', 'speakers']
    ordering_fields = ['scheduled_date', 'created_at', 'title']
    ordering = ['-scheduled_date', '-created_at']


class PodcastPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class PodcastViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Podcasts
    
    Provides list, retrieve, create, update, and destroy actions
    Filters by category
    Search by title, description, host, guest, and tags
    """
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    pagination_class = PodcastPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'description', 'host', 'guest', 'tags']
    ordering_fields = ['published_date', 'created_at', 'title']
    ordering = ['-published_date', '-created_at']


class GalleryPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class GalleryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Gallery Images
    
    Provides list, retrieve, create, update, and destroy actions
    Filters by category and featured status
    Search by title, description, photographer, and tags
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = GalleryPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['title', 'description', 'photographer', 'tags']
    ordering_fields = ['event_date', 'created_at', 'title']
    ordering = ['-featured', '-event_date', '-created_at']
