from rest_framework import serializers
from messages.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id",
                  "user",
                  "message")
        
