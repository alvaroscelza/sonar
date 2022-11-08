from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from applications.core.models import Post


@login_required
def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})
