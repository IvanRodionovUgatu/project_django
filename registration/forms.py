from django import forms
from .models import Profile, Message


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']