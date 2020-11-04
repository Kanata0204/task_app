from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.models import Group

from registration import views

admin.site.unregister(Group)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskapp.urls')),
    path("", include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name="activate")
]
