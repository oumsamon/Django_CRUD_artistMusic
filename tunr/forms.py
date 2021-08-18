from django import forms
from .models import Artist, Song

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        # exclude = ('1','2')
        fields = ('name', 'photo_url', 'nationality')