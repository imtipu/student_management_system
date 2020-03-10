from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dashboard.api.v1 import views as api_views, viewsets

router = DefaultRouter()

urlpatterns = [
    path('dashboard/counter/', api_views.DashboardCounters.as_view()),
    path('dashboard/index_data/', api_views.DashboardIndexData.as_view()),
]