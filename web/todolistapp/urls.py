from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoDeleteView, TodoUpdateView

app_name = 'todolistapp'
urlpatterns = [
    path(route='', view=TodoListView.as_view(), name='todo_list'),
    path(route='<int:pk>', view=TodoDetailView.as_view(), name='todo_detail'),
    path(route='delete/<int:pk>', view=TodoDeleteView.as_view(), name='todo_delete'),
    path(route='edit/<int:pk>', view=TodoUpdateView.as_view(), name='todo_edit'),
    path(route='novo/', view=TodoCreateView.as_view(), name='todo_new')
]

