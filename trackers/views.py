from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .models import Bill, BillReading, MP, DebtData, Loan, Hansard, Budget
from .serializers import BillSerializer, BillListSerializer, BillReadingSerializer, MPListSerializer, MPDetailSerializer, DebtDataSerializer, LoanSerializer, HansardSerializer, BudgetSerializer


class BillViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing bills.
    """
    queryset = Bill.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['bill_type', 'status', 'year_introduced']
    search_fields = ['title', 'mover', 'assigned_to']
    ordering_fields = ['created_at', 'year_introduced', 'title']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return BillListSerializer
        return BillSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """Increment the like count for a bill"""
        bill = self.get_object()
        bill.likes += 1
        bill.save()
        return Response({'likes': bill.likes})

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        """Increment the comment count for a bill"""
        bill = self.get_object()
        bill.comments += 1
        bill.save()
        return Response({'comments': bill.comments})

    @action(detail=True, methods=['post'])
    def share(self, request, pk=None):
        """Increment the share count for a bill"""
        bill = self.get_object()
        bill.shares += 1
        bill.save()
        return Response({'shares': bill.shares})


class BillReadingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing bill readings.
    """
    queryset = BillReading.objects.all()
    serializer_class = BillReadingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bill', 'stage']


class MPPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class MPViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Members of Parliament

    Provides list, retrieve, create, update, and destroy actions
    Filters by party, district, and constituency
    Search by name, constituency, and district
    """
    queryset = MP.objects.all()
    pagination_class = MPPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['party', 'district', 'constituency']
    search_fields = ['name', 'first_name', 'last_name', 'constituency', 'district']
    ordering_fields = ['name', 'last_name', 'district', 'created_at']
    ordering = ['last_name', 'first_name']

    def get_serializer_class(self):
        """Use different serializers for list and detail views"""
        if self.action == 'list':
            return MPListSerializer
        return MPDetailSerializer


class DebtDataViewSet(viewsets.ModelViewSet):
    """
    ViewSet for National Debt and Economic Data

    Provides historical debt and economic metrics
    """
    queryset = DebtData.objects.all().order_by('year')
    serializer_class = DebtDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['year']
    ordering_fields = ['year']
    ordering = ['year']

    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Get the latest debt data"""
        latest_data = DebtData.objects.order_by('-year').first()
        if latest_data:
            serializer = self.get_serializer(latest_data)
            return Response(serializer.data)
        return Response({})


class LoanPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class LoanViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Government Loans

    Provides loan data with filtering by sector and source
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    pagination_class = LoanPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['sector', 'currency', 'source']
    search_fields = ['label', 'description', 'sector']
    ordering_fields = ['approved_amount', 'approval_date', 'created_at']
    ordering = ['-approval_date', '-created_at']

    @action(detail=False, methods=['get'])
    def sources_summary(self, request):
        """Get loan sources summary for pie chart"""
        sources = Loan.objects.values('source').annotate(
            count=Count('id')
        ).order_by('-count')

        # Calculate percentages
        total = sum(item['count'] for item in sources)
        summary = []
        for item in sources:
            source_obj = Loan.objects.filter(source=item['source']).first()
            summary.append({
                'source': item['source'],
                'name': source_obj.get_source_display() if source_obj else item['source'],
                'count': item['count'],
                'percentage': round((item['count'] / total * 100), 1) if total > 0 else 0
            })

        return Response(summary)


class HansardPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


class HansardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Hansards

    Provides parliamentary hansard records with file downloads
    """
    queryset = Hansard.objects.all()
    serializer_class = HansardSerializer
    pagination_class = HansardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['date']
    search_fields = ['name']
    ordering_fields = ['date', 'created_at', 'name']
    ordering = ['-date', '-created_at']


class BudgetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


class BudgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Budgets

    Provides national budget documents with file downloads
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    pagination_class = BudgetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['financial_year']
    search_fields = ['name', 'financial_year']
    ordering_fields = ['financial_year', 'created_at', 'name']
    ordering = ['-financial_year', '-created_at']