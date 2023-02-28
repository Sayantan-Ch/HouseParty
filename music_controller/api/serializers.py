from rest_framework import serializers
from .models import Room

# Used to serialize data what this means that all the model data in backend can be send to frontend but this isnt in JSON format with this way we serialize the data and can send it then 
# Id is a inbuilt made field always made in models it acts as a primary key

# Always use a serialize to handle different request either an incoming one to handle request or outgoing one to handle response

# This one is used to serialize a room object and send it back as a response
class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id','code','host','guest_can_pause','votes_to_skip','created_at')



# This one is used to serialize the request we get to make a room, POST Request
class CreateRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('guest_can_pause','votes_to_skip')