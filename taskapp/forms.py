from django import forms
from django.forms import fields
from .models import Task

class TaskForm(forms.ModelForm):

    content = forms.CharField(widget=forms.TextInput(attrs={"size":50}))

    class Meta:
        model = Task
        # 例え、id=1, content = ...のような悪意のあるフォームが送られても無視できる
        fields = ["content", ]
    pass