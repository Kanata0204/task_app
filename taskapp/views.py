from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskListView(ListView):
    model = Task

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm

    success_url = reverse_lazy("list")

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        # pk取得
        task_pk = self.kwargs['pk']
        # task_pkのdetailへアクセス
        url = reverse_lazy("detail", kwargs={"pk":task_pk})
        return url

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("list")