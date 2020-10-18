from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Task

# Create your views here.
class TaskListView(ListView):
    model = Task

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    # 例え、id=1, content = ...のような悪意のあるフォームが送られても無視できる
    fields = ["content", ]
    success_url = reverse_lazy("list")

class TaskUpdateView(UpdateView):
    model = Task
    fields = ["content", ]

    def get_success_url(self):
        # pk取得
        task_pk = self.kwargs['pk']
        # task_pkのdetailへアクセス
        url = reverse_lazy("detail", kwargs={"pk":task_pk})
        return url