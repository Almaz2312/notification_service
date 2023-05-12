from rest_framework.urls import path

from message.views import MessageListView

urlpatterns = [
    path('', MessageListView.as_view(), name='message')
]