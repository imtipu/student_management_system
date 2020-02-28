from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class StudentClass(models.Model):
    title = models.CharField(max_length=120, default=None, null=False, help_text='Add Class Title')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.title


class StudentsInClass(models.Model):
    student = models.ForeignKey(
        'users.User',
        default=None,
        null=False,
        on_delete=models.CASCADE,
        related_name='studentsinclass_student',
        help_text='Select Student'
    )

    student_class = models.ForeignKey(
        'students.StudentClass',
        default=None,
        null=False,
        on_delete=models.CASCADE,
        related_name='studentsinclass_class',
        help_text='Select Class'
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Stundents in Class'
        verbose_name_plural = 'Stundents in Class'

    def __unicode__(self):
        return u'%s' % self.pk