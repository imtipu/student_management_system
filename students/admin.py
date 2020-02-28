from django.contrib import admin

# Register your models here.
from students.models import *


@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'created',
        'updated',
    ]


@admin.register(StudentsInClass)
class StudentsInClassAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'student',
        'student_class',
        'created',
        'updated',
    ]