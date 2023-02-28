
from django.urls import path
from .views import RoomView , CreateRoomView

urlpatterns = [
    path('viewRooms',RoomView.as_view()),
    path('create-room',CreateRoomView.as_view())
]
