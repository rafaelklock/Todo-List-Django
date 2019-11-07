from django.urls import path
from .views import ListView, DetailView

app_name = 'todolistapp'
urlpatterns = [
    path(route='', view=ListView.as_view(), name='todo_list'),
    path(route='<int:pk>', view=DetailView.as_view(), name='todo_detail'),
]

