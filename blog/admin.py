from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description']
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fileds to search in change list
    search_fields = ['title', 'description', 'content']
    # enable the date dirll down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top of change form
    save_on_top = True
    # prepopulate the slug from the title
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post, PostAdmin)