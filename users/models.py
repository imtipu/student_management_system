from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=None, null=True,)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.username

    @property
    def full_name(self):
        if self.first_name:
            return u'{} {}'.format(self.first_name, self.last_name)
        else:
            return u'%s' % self.username
