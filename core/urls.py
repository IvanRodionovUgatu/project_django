from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('redirect/', Redirect.as_view(), name='redirect'),
    path('info/', Info.as_view(), name='info'),
    path('teachers/', Teachers.as_view(), name='teachers'),
    path('subjects/', Subjects.as_view(), name='subjects'),
    path('teacher/<id>/', Teacher.as_view(), name='teacher'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
