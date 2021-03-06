from os import name
from django.urls import path
from .views import TaskDetailView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskIndexView, TaskMainView

urlpatterns = [
    path('', TaskIndexView.as_view(), name="index"),
    path('task_list/', TaskListView.as_view(), name="list"),
    path('task_list/main', TaskMainView.as_view(), name="main"),
    # pkは受け取ったint値を変数として格納→templateで扱えるように
    path('task_list/<int:pk>', TaskDetailView.as_view(), name="detail"),
    path('task_list/create/', TaskCreateView.as_view(), name="create"),
    path('task_list/<int:pk>/update', TaskUpdateView.as_view(), name="update"),
    path('task_list/<int:pk>/delete', TaskDeleteView.as_view(), name="delete"),
]
