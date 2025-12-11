from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Objective, TeamMember
from .serializers import ObjectiveSerializer, TeamMemberSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Objectives
    
    Provides list, retrieve, create, update, and destroy actions
    Filters by is_active
    """
    queryset = Objective.objects.filter(is_active=True).order_by('order', 'created_at')
    serializer_class = ObjectiveSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['order', 'created_at']
    ordering = ['order', 'created_at']
    http_method_names = ['get', 'head', 'options']  # Read-only for public


class TeamMemberViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Team Members
    
    Provides list, retrieve, create, update, and destroy actions
    Filters by is_active
    """
    queryset = TeamMember.objects.filter(is_active=True).order_by('order', 'name')
    serializer_class = TeamMemberSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    http_method_names = ['get', 'head', 'options']  # Read-only for public
