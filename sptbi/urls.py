from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('apply/', include('apply.urls')),
    path('hire/', include('hire.urls')),
    path('api/gl/', include('social_django.urls',namespace='social')),
    # path('apply/login/', include('social_django.urls',namespace='social')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)