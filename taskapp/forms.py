from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from .models import Task

class TaskForm(forms.ModelForm):

    title = forms.CharField(label="タスク名", widget=forms.TextInput(), help_text="※必須")
    day_limit = forms.DateField(label='期限日',widget=forms.DateInput(attrs={"type":"date"}), required=False, help_text="※任意")
    time_limit = forms.TimeField(label='時間の期限', widget=forms.TimeInput(attrs={"type":"time"}), required=False, help_text="※任意")
    memo = forms.CharField(label="メモ", widget=forms.Textarea(), required=False, help_text="※任意")

    class Meta:
        model = Task
        # 例え、id=1, content = ...のような悪意のあるフォームが送られても無視できる
        fields = '__all__'