from django.shortcuts import render, get_object_or_404
from blog.models import Post

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