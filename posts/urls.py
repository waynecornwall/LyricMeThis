from django.urls import path
from . import views

app_name = 'posts'

# URL pattern for...
urlpatterns = [
    # ...homepage
    path('', views.index, name='index'),

    # ...songs page
    path('songs/', views.songs, name='songs'),

    # ...song page
    path('songs/<int:song_id>/', views.song, name='song'),

    # ...new song page
    path('new_song/', views.new_song, name='new_song'),

    # ...edit song page
    path('edit_song/<int:song_id>/', views.edit_song, name='edit_song'),

    # ...delete song page
    path('songs/<int:song_id>/delete/', views.delete_song, name='delete_song')
]