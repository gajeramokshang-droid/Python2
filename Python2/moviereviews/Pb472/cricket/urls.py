from .import views
from django.urls import path

urlpatterns=[
    path('home/',views.home,name="home"),
    path('detail/<int:player_id>',views.player_detail,name='player_detail'),
    path('player/',views.add_player,name='add_player')
]