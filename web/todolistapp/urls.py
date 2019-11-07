from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView

app_name = 'todolistapp'
urlpatterns = [
    path(route='', view=TodoListView.as_view(), name='todo_list'),
    path(route='<int:pk>', view=TodoDetailView.as_view(), name='todo_detail'),
    path(route='novo/', view=TodoCreateView.as_view(), name='todo_new')
]

