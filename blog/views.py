from django.shortcuts import render, get_object_or_404, render_to_response
from blog.models import Post, Category, Tag
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.


def index(request):
    # get blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog_posts.html', {'posts': posts})


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # return the rendered template
    return render(request, 'blog_post.html', {'post': post})


def getSearchResults(request):
    """
    Search for a post by title or text
    """
    # Get the query data
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    # Query the database
    if query:
        results = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query) | Q(category__name__icontains=str(query)))
    else:
        results = None
    # Add pagination
    pages = Paginator(results, 5)
    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    # Display the search results
    return render_to_response('blog/post_list.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': query})


class CategoryListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()


class TagListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            return tag.post_set.all()
        except Tag.DoesNotExist:
            return Post.objects.none()
