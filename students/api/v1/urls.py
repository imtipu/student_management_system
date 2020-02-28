from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.api.v1 import views as api_views, viewsets

router = DefaultRouter()
router.register(u'students', viewsets.StudentViewSet, basename='students')
router.register(u'classes', viewsets.StudentClassViewSet, basename='classes')
# router.register(u'students', viewsets.StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]