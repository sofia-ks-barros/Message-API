from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from messages.models import Message
from messages.serializers import MessageSerializer
from adrf.decorators import api_view
from rest_framework.decorators import permission_classes
# Create your views here.

def method_get_list(*ignore):
    messages = Message.objects.all()
    messages_serializer = MessageSerializer(messages, many=True)
    return JsonResponse(messages_serializer.data, safe=False)

def method_post_list(request):
    message_data = JSONParser().parse(request)
    messages_serializer = MessageSerializer(data=message_data)
    if  messages_serializer.is_valid():
        messages_serializer.save()
        return JsonResponse(messages_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_delete_list(*ignore):
    count = Message.objects.all().delete()
    return JsonResponse({"message": f"{count} messages were deleted successfully!"})


methods_list={"GET": method_get_list,
         "POST": method_post_list,
         "DELETE": method_delete_list   
        }

@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def message_list(request):
    return methods_list[request.method](request)

@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def message_detail(request, pk):
    try:
        tutorial = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return JsonResponse({"message": "The tutorial does not exist"})