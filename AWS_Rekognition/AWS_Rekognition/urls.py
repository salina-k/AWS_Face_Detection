from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ImageUpload.views import ImageUploadView, success, display_upload_images

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload', ImageUploadView, name='image_upload'),
    path('success', success, name='success'),
    # path('analysis', display_upload_images),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



