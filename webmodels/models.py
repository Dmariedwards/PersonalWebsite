from django.db import models
from django.forms import forms
from django.db.models import FileField, DateTimeField, EmailField, BooleanField, ImageField


class Section(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField(
        max_length=500,
        unique=False,
        null=True,
        blank=True,
    )
    pdffile = FileField(upload_to='media/files')
    image = ImageField(upload_to='media/images')
    created = models.DateTimeField('created', 
        auto_now_add=True)
    modified = models.DateTimeField('modified',
        auto_now=True)




class User(models.Model):
    """Admin Model"""
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100, unique=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField()
    is_authenticated = models.BooleanField()
    last_login = models.DateTimeField(blank=True, null=True)

    is_superuser = models.BooleanField()
    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Returns the first name + lastname  with a  space inbetween
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()