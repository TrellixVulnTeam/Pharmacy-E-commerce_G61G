from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *
from .router import router
from rest_framework.authtoken import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/', include(router.urls), name='api'),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
