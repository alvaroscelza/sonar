from django.contrib.auth import get_user_model
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
    post.views_amount += 1
    post.save()
    ActivityLog.objects.create(user=request.user, interaction_type=ActivityLog.InteractionTypes.VIEW)
    return render(request, 'posts/detail.html', {'post': post})


@login_required
@require_http_methods(["POST"])
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes_amount += 1
    post.save()
    ActivityLog.objects.create(user=request.user, interaction_type=ActivityLog.InteractionTypes.LIKE)
    return render(request, 'posts/detail.html', {'post': post})


@require_http_methods(["GET"])
def dashboard(request):
    users_amount = get_user_model().objects.count()
    most_viewed_posts = Post.objects.order_by('-views_amount')[:5]
    most_liked_posts = Post.objects.order_by('-likes_amount')[:5]
    context = {'users_amount': users_amount, 'most_viewed_posts': most_viewed_posts,
               'most_liked_posts': most_liked_posts}
    return render(request, 'dashboard/index.html', context)
