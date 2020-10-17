from django.urls import path
from .views import TaskDetailView, TaskListView

urlpatterns = [
    path('task_list/', TaskListView.as_view(), name="list"),
    # pkは受け取ったint値を変数として格納→templateで扱えるように
    path('task_list/<int:pk>', TaskDetailView.as_view(), name="detail")
]
