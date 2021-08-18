from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('songs/', views.song_list, name='song_list'),
    path('artists/new', views.artist_create, name='artist_create'),
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('songs/<int:pk>', views.song_detail, name='song_detail'),
]


# express.js
# app.get('/')
# app.get('/songs')
