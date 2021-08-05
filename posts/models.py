""" Posts models. """ 

import uuid
# Django
from django.db import models

class User(models.Model):
    """ User model. """
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(max_length=500, blank=True, null=True)

    birthday = models.DateField(null=True, blank=True)

    country = models.CharField(max_length=3, default='MX')
    city = models.CharField(max_length=200, default='CDMX')

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        """ Return email."""
        return self.email