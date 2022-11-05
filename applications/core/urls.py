from django.urls import path

from applications.core import views

urlpatterns = [
    path('posts', views.get_posts, name='posts'),
]
