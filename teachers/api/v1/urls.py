from django.urls import path, include
from rest_framework.routers import DefaultRouter

from teachers.api.v1 import views as api_views, viewsets

router = DefaultRouter()
router.register(u'teachers', viewsets.TeacherViewSet, basename='teachers')
# router.register(u'students', viewsets.StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]