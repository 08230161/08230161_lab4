from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Homepage URL
    path('about/', views.about_me, name='aboutMe'),  # About Me page URL
]
