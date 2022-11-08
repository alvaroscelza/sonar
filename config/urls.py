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
    path('', views.get_posts, name='posts'),
    path('<post_id>', views.get_post, name='post'),
]
# endregion
