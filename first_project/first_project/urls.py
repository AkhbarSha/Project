from django.urls import path
from first_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.upload_image, name='upload'),
    path('result/', views.detect_faces, name='result'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)