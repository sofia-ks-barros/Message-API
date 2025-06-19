from django.urls import re_path
from MessagesApp import views

urlpatterns = [
    re_path(r"^api/chats", views.chat_list),
    re_path(r"^api/messages", views.chat_message_list),
    #re_path(r"^api/chats/messages/(?P<pk>[0-9]+)$", views.chat_messages_detail),
    re_path(r"^api/user", views.user_list),
    #re_path(r"^api/chats/messages/(?P<pk>[0-9]+)$", views.message_detail),
    #re_path(r"^api/messages$", views.message_list),
    
]