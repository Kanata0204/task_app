from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from .models import Task

class TaskForm(forms.ModelForm):

    title = forms.CharField(label="タスク名", widget=forms.TextInput(attrs={"size":50}))
    time_limit = forms.DateTimeField(label='期限', widget=forms.DateTimeInput(attrs={"type":"date"}), required=False)
    memo = forms.CharField(label="備考", widget=TextInput(), required=False)

    class Meta:
        model = Task
        # 例え、id=1, content = ...のような悪意のあるフォームが送られても無視できる
        fields = ["title", "time_limit","memo", ]