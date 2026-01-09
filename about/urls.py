from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ObjectiveViewSet, TeamMemberViewSet, WhoWeAreViewSet,
    OurStoryViewSet, WhatSetsUsApartViewSet, PartnerViewSet
)

router = DefaultRouter()
router.register(r'objectives', ObjectiveViewSet, basename='objective')
router.register(r'team-members', TeamMemberViewSet, basename='team-member')
router.register(r'who-we-are', WhoWeAreViewSet, basename='who-we-are')
router.register(r'our-story', OurStoryViewSet, basename='our-story')
router.register(r'what-sets-us-apart', WhatSetsUsApartViewSet, basename='what-sets-us-apart')
router.register(r'partners', PartnerViewSet, basename='partner')

urlpatterns = [
    path('', include(router.urls)),
]


