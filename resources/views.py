from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Explainers, Report, PartnerPublication, Statement
from .serializers import ExplainersSerializer, ReportSerializer, PartnerPublicationSerializer, StatementSerializer


class ResourcePagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


class ExplainersViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Explainers

    Provides educational explainer documents
    """
    queryset = Explainers.objects.all()
    serializer_class = ExplainersSerializer
    pagination_class = ResourcePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']


class ReportViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Reports & Briefs

    Provides reports and brief documents
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    pagination_class = ResourcePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']


class PartnerPublicationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Partner Publications

    Provides partner publication documents
    """
    queryset = PartnerPublication.objects.all()
    serializer_class = PartnerPublicationSerializer
    pagination_class = ResourcePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']


class StatementViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Statements

    Provides official statement documents
    """
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    pagination_class = ResourcePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    ordering = ['-created_at']