from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExplainersViewSet, ReportViewSet, PartnerPublicationViewSet, StatementViewSet, HomeResourcesSummaryView

router = DefaultRouter()
router.register(r'explainers', ExplainersViewSet, basename='explainer')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'partner-publications', PartnerPublicationViewSet, basename='partner-publication')
router.register(r'statements', StatementViewSet, basename='statement')

urlpatterns = [
    path('home-summary/', HomeResourcesSummaryView.as_view(), name='home-resources-summary'),
    path('', include(router.urls)),
]