from django.db import models

# Create your models here.
from django.db import models

class Land(models.Model):
    object_title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    aboutme_heading = models.CharField(max_length=255)
    aboutme_text = models.TextField()
    aboutblog_heading = models.CharField(max_length=255)
    aboutblog_text = models.TextField()
    contact_heading = models.CharField(max_length=255)
    contact_text = models.TextField()