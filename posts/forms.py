from .models import Song
from django.contrib.auth.forms import forms


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'lyrics']
        labels = {
            'title' : '',
            'lyrics' : ''
        }
        widgets = {
            'lyrics' : forms.Textarea(attrs={'cols' : 80})
        }