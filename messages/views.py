from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from messages.models import Message, User, Chat
from messages.serializers import MessageSerializer
from messages.serializers import UserSerializer
from messages.serializers import ChatSerializer
from adrf.decorators import api_view
from rest_framework.decorators import permission_classes
# Create your views here.

def chat_messages_method_get_list(request):
    from_chat = JSONParser.parse(request)["from_chat"]
    if not from_chat:
        return JsonResponse({"error": "You need to choose a chat."}, status=status.HTTP_400_BAD_REQUEST)
    
    messages = Message.objects.filter(from_chat__contains=from_chat)    
    messages_serializer = MessageSerializer(messages, many=True)
    return JsonResponse(messages_serializer.data, safe=False)
def chat_messages_method_post_list(request):    
    message_data = JSONParser().parse(request)
    messages_serializer = MessageSerializer(data=message_data)
    if  messages_serializer.is_valid():
        messages_serializer.save()
        return JsonResponse(messages_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def chat_messages_method_delete_list(request):
    from_chat = JSONParser.parse(request)["from_chat"]
    count = Message.objects.filter(from_chat__contains=from_chat).delete()
    return JsonResponse({"message": f"{count} messages from {from_chat} were deleted successfully!"})

chat_message_methods_list={
         "GET": chat_messages_method_get_list,
         "POST": chat_messages_method_post_list,
         "DELETE": chat_messages_method_delete_list   
        }

def user_method_get():
    user = User.objects.all()
    user_serializer = UserSerializer(user, many=True)
    return JsonResponse(user_serializer.data, safe=False)
def user_method_post(request):    
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    if  user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def user_method_delete(request):
    user = JSONParser.parse(request)
    User.objects.filter(user).delete()
    return JsonResponse({"message": f"User {user.username} was deleted successfully!"})

user_methods_list={
         "GET": user_method_get,              
         "POST": user_method_post,
         "DELETE": user_method_delete   
        }

def chat_method_get():
    chat = User.objects.all()    
    chat_serializer = ChatSerializer(chat, many=True)
    return JsonResponse(chat_serializer.data, safe=False)
def chat_method_post(request):    
    chat_data = JSONParser().parse(request)
    chat_serializer = ChatSerializer(data=chat_data)
    if  chat_serializer.is_valid():
        chat_serializer.save()
        return JsonResponse(chat_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(chat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def chat_method_delete(request):
    chat = JSONParser.parse(request)
    Chat.objects.filter(chat).delete()
    return JsonResponse({"message": f"Chat {chat.name} was deleted successfully!"})

chat_methods_list={
         "GET": chat_method_get,       
         "POST": chat_method_post,
         "DELETE": chat_method_delete   
        }


@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def chat_message_list(request):
    return chat_message_methods_list[request.method](request)

@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def chat_list(request):
    return chat_message_methods_list[request.method](request)

@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def user_list(request):
    return chat_message_methods_list[request.method](request)