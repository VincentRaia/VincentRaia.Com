from django.shortcuts import render
from django.template import Context, loader
from landing.models import Land
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    # get the Post object
    content = get_object_or_404(Land, object_title="Live")
    return render(request, 'landing.html', {'content': content})