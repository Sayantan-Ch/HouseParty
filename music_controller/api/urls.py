
from django.urls import path
from .views import RoomView 
from .views import createRoom

urlpatterns = [
    path('viewRooms',RoomView.as_view()),
    path('createRooms',createRoom.as_view())
]
