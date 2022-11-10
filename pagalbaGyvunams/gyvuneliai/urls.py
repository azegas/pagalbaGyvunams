from django.urls import path
from . import views

# this way of hosting images is not the best for production
from django.conf.urls.static import static
from django.conf import settings  # use the settings from settings.py file

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/', views.post, name="post"),
]

# good explanation here at 7:50 - https://www.youtube.com/watch?v=aNk2CAkHvlE&ab_channel=DennisIvy
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# check here - http://127.0.0.1:8000/media/photo/2022/1110/vilkiukai.jpg

# if not all db entires have images assigned you might get this error
# ValueError: The 'photo' attribute has no file associated with it.
