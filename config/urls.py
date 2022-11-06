from django.conf import settings
from django.conf.urls.static import static
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
    path('', views.get_posts, name='posts'),
    path('login/', RedirectView.as_view(pattern_name='posts')),
]
# endregion

# region Media configuration
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# endregion
