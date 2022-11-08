from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from applications.core.models import Post, ActivityLog


@login_required
@require_http_methods(["GET"])
def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
@require_http_methods(["GET"])
def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})


@login_required
@require_http_methods(["POST"])
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes_amount += 1
    post.save()
    ActivityLog.objects.create(user=request.user, interaction_type=ActivityLog.InteractionTypes.LIKE)
    return render(request, 'posts/detail.html', {'post': post})
