from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from applications.core import views

# region Admin configuration
urlpatterns = [path('admin/', admin.site.urls)]
admin.site.site_header = settings.APP_NAME
admin.site.index_title = settings.APP_DESCRIPTION
admin.site.site_title = settings.APP_NAME
# endregion

# region Core configuration
urlpatterns += [
    path('login/', RedirectView.as_view(pattern_name='posts')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<post_id>/', views.get_post, name='post'),
    path('<post_id>/like/', views.like_post, name='like_post'),
    path('', views.get_posts, name='posts'),
]
# endregion
