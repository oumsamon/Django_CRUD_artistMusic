from django.shortcuts import render, redirect

# Create your views here.

from .models import Artist, Song
from .forms import ArtistForm

def artist_list(request):
   
    artists = Artist.objects.all()
    artists = artists.order_by('name')
   
    # artists = list(artists)
    # artists.sort(lambda e: e[1])

    print(artists)

    return render(
            request, 
            'tunr/artist_list.html', 
            {'artists':artists},
            )


def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
        else:
            form = ArtistForm()
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form':form})


def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk) # Todo.findById(req.params.id)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})

def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})

def artist_detail(request, pk):
    
    try:
        artist = Artist.objects.get(id=pk)
    except:
        artist = {
            'name': "No artist found", 
            'nationality': f'with id {pk}'
            }
        print(f"artist with id={pk} didn't work")
    
    return render(request, 'tunr/artist_detail.html', {'artist': artist})