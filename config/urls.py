from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

# region Core configuration
urlpatterns = [path('core/', include('applications.core.urls'))]
# endregion

# region Media configuration
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# endregion

# region Templates configuration
urlpatterns.append(path('', TemplateView.as_view(template_name='index.html')))
# endregion
