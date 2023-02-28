from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializers , CreateRoomSerializers
# Create your views here.

class RoomView(generics.ListAPIView):
    queryset= Room.objects.all()
    serializer_class = RoomSerializers

# APIView basically overides default methods

class CreateRoomView(APIView):
    
    serializer_class = CreateRoomSerializers

    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer =  self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause=serializer.data.get('guest_can_pause')
            votes_to_skip=serializer.data.get('votes_to_skip')
            host=self.request.session.session_key
            # We are doing this so that if a host again joins we dont make new room rather just update old room settings
            querySet=Room.objects.filter(host=host)
            if querySet.exists():
                room=querySet[0]
                room.guest_can_pause=guest_can_pause
                room.votes_to_skip=votes_to_skip
                room.save(update_fields=['guest_can_pause','votes_to_skip'])
            else:
                room=Room(host=host,guest_can_pause=guest_can_pause,votes_to_skip=votes_to_skip)
                room.save()
            return Response(RoomSerializers(room).data,status=status.HTTP_200_OK)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

