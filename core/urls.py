from django.urls import path

from core.views import Home, Teachers, Subjects

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('teachers/', Teachers.as_view(), name='teachers'),
    path('subjects/', Subjects.as_view(), name='subjects')
]
