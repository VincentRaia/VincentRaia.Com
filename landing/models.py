from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class Land(models.Model):
    object_title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    aboutme_heading = models.CharField(max_length=255)
    aboutme_text = RichTextField()
    aboutblog_heading = models.CharField(max_length=255)
    aboutblog_text = RichTextField()
    contact_heading = models.CharField(max_length=255)
    contact_text = RichTextField()