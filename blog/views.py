from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    post = Post.objects.all()
    context = {
        'posts':post
    }
    return render(request,'blog/index.html',context)