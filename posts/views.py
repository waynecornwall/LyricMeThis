from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'posts/index.html')


@login_required
def songs(request):
    """ List of all user's songs """
    # Get all songs
    all_songs = Song.objects.filter(author=request.user).order_by('-date_posted')
    song_count = len(all_songs)
    # Render page
    context = {
        'all_songs' : all_songs,
        'song_count' : song_count
    }
    return render(request, 'posts/songs.html', context)


@login_required
def song(request, song_id):
    """ Displays specific song """
    # Get a specific song
    song = Song.objects.get(id=song_id)
    if song.author != request.user:
        raise Http404
    # Render page
    context = {
        'song' : song
    }
    return render(request, 'posts/song.html', context)


@login_required
def new_song(request):
    """ Create a new song """
    # Display blank form
    if request.method != 'POST':
        form = SongForm()
    # Process filled out form
    else:
        form = SongForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:song', song_id = new_post.id)
    # Render page if request == GET or form is invalid
    context = {
        'form' : form
    }
    return render(request, 'posts/new_song.html', context)


@login_required
def edit_song(request, song_id):
    """ Edits existing song """
    # Grab existing song from database
    song = Song.objects.get(id=song_id)
    if song.author != request.user:
        raise Http404
    # Display pre-filled out form
    if request.method != 'POST':
        form = SongForm(instance=song)
    # Process form with changes
    else:
        form = SongForm(instance=song, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:song', song_id = song_id)
    # Render page if request.method is get or forms are invalid
    context = {
        'song' : song,
        'form' : form
    }
    return render(request, 'posts/edit_song.html', context)


# @login_required
# def delete_song(request, song_id):
#     songs = Song.objects.all()
#     for song in songs:
#         if song.author != request.user:
#             raise Http404
#         if song_id == song.id:
#             del song
#             return redirect('posts:songs')
#     context = {
#         'songs' : songs
#     }
#     return render(request, 'posts/delete_song.html', context)

