from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from registration.views import Registration

urlpatterns = [
    path('', Registration.as_view(), name='registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
