from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from registration.views import *

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
