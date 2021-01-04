from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('', include('page.urls')),
    path('admin/', admin.site.urls),
    path('article/', include('article.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 


handler404='page.views.error_404_view'


if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
