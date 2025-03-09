from django.urls import re_path
from messages import views

urlpatterns = [
    re_path(r"^api/messages$", views.message_list),
    re_path(r"^api/messages/(?P<pk>[0-9]+)$", views.message_detail),
]