from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('movies.urls')),   
    path('events/', include('events.urls')),
    path('bookings/', include('bookings.urls')),
    path('seats/', include('seats.urls')),
    path('reviews/', include('reviews.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(getattr(settings, 'MEDIA_URL', '/media/'), document_root=getattr(settings, 'MEDIA_ROOT', 'media'))
