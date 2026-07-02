from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               
    path('welcome/', views.welcome, name='welcome'),
    path("add_player/",views.add_player),
    path("edit_player/<int:player_id>",views.edit_player),
    path('delete/<int:player_id>',views.delete_player)
]
