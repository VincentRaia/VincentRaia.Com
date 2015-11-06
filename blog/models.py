# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super(Category, self).save()

    def get_absolute_url(self):
        return "/categories/%s/" % (self.slug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super(Tag, self).save()

    def get_abosulte_url(self):
        return "/tag/%s/" % (self.slug)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = RichTextField()
    content = RichTextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return 'blog/ %s' % reverse('blog.views.post', args=[self.slug])

