from rest_framework import serializers
from messages.models import Message, User, Chat

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id",
                  "user",
                  "message",
                  "created_date",
                  "from_chat"
                  )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "password",
                  "created_date",
                  "display_name"
                  )
    
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("name",
                  "created_date",
                  "messages_amount"
                  )