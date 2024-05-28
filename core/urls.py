from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacher_rest', TeacherRest, basename='teacher_rest')

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('redirect/', Redirect.as_view(), name='redirect'),
    path('info/', Info.as_view(), name='info'),
    path('teachers/', Teachers.as_view(), name='teachers'),
    path('subjects/', Subjects.as_view(), name='subjects'),
    path('add_subject/', AddSubject.as_view(), name='add_subject'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('subjects_rest/', SubjectRest.as_view(), name='subjects_rest'),
    path('subjects_rest/<int:pk>/', SubjectRest.as_view(), name='subject_detail_rest'),
    path('teacher/<id>/', Teacher.as_view(), name='teacher'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),
    path('add_teacher/', AddTeacher.as_view(), name='add_teacher'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
