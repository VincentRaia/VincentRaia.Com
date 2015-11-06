from django.shortcuts import render, get_object_or_404, render_to_response
from blog.models import Post
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

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
        results = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
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
    return render_to_response('search.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': query})