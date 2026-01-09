from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Objective, TeamMember, WhoWeAre, OurStory, WhatSetsUsApart, Partner
from .serializers import (
    ObjectiveSerializer, TeamMemberSerializer, WhoWeAreSerializer,
    OurStorySerializer, WhatSetsUsApartSerializer, PartnerSerializer
)


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


class WhoWeAreViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Who We Are section
    """
    queryset = WhoWeAre.objects.filter(is_active=True).order_by('-updated_at')
    serializer_class = WhoWeAreSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['updated_at', 'created_at']
    ordering = ['-updated_at']
    http_method_names = ['get', 'head', 'options']  # Read-only for public


class OurStoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Our Story section
    """
    queryset = OurStory.objects.filter(is_active=True).order_by('-updated_at')
    serializer_class = OurStorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['updated_at', 'created_at']
    ordering = ['-updated_at']
    http_method_names = ['get', 'head', 'options']  # Read-only for public


class WhatSetsUsApartViewSet(viewsets.ModelViewSet):
    """
    ViewSet for What Sets Us Apart items
    """
    queryset = WhatSetsUsApart.objects.filter(is_active=True).order_by('order', 'created_at')
    serializer_class = WhatSetsUsApartSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['order', 'created_at']
    ordering = ['order', 'created_at']
    http_method_names = ['get', 'head', 'options']  # Read-only for public


class PartnerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Partners
    """
    queryset = Partner.objects.filter(is_active=True).order_by('order', 'name')
    serializer_class = PartnerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']
    http_method_names = ['get', 'head', 'options']  # Read-only for public
