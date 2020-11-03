from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.models import Group

admin.site.unregister(Group)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskapp.urls')),
    path("", include('django.contrib.auth.urls')),
]
