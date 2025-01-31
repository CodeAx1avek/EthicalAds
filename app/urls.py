from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-ad/', views.generate_ad, name='generate_ad'),
    path('insight/', views.insight, name='insight'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)