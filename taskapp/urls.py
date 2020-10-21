from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import TaskDetailView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('task_list/', TaskListView.as_view(), name="list"),
    # pkは受け取ったint値を変数として格納→templateで扱えるように
    path('task_list/<int:pk>', TaskDetailView.as_view(), name="detail"),
    path('task_list/create/', TaskCreateView.as_view(), name="create"),
    path('task_list/<int:pk>/update', TaskUpdateView.as_view(), name="update"),
    path('task_list/<int:pk>/delete', TaskDeleteView.as_view(), name="delete"),
    path('task_list/login', LoginView.as_view(template_name="login.html"), name='login'),
    path('task_list/logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
]
