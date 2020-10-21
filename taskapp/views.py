from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 5

class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "taskapp/task_create_form.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list")

    login_url = '/login'

    # 正しく作成できた時
    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存できませんでした")
        return super().form_invalid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "taskapp/task_update_form.html"
    model = Task
    form_class = TaskForm

    # ログインしていないユーザが編集しようとすると強制的にリダイレクトさせる
    login_url = '/login'

    def get_success_url(self):
        # pk取得
        task_pk = self.kwargs['pk']
        # task_pkのdetailへアクセス
        url = reverse_lazy("detail", kwargs={"pk":task_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "問題により更新できませんでした")
        return super().form_invalid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("list")

    login_url = '/login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)