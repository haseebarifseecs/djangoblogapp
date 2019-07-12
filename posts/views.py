from django.shortcuts import render
from .models import Post



def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/blog.html', context)
