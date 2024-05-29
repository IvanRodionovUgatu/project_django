from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from registration.views import *

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:user_id>/', Profile.as_view(), name='profile'),
    path('profile_edit/', ProfileEdit.as_view(), name='profile_edit'),
    path('send_message/<int:pk>/', SendMessage.as_view(), name='send_message'),
    path('message_list/<int:pk>/', MessageList.as_view(), name='message_list'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('delete_post/<int:pk>/', PostDelete.as_view(), name='delete_post'),
    path('delete_comment/<int:pk>/', CommentDelete.as_view(), name='delete_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
