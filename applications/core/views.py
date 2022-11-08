from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from applications.core.models import Post


@login_required
def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def get_post(request, post_id):
    return render(request, 'posts/detail.html')
