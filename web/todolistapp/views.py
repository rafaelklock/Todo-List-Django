from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo


class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    success_url = reverse_lazy('todolistapp:todo_list')
    fields = ['todo', 'done']
