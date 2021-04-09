from django.db import models
from registration.models import CustomUser
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザ', on_delete=models.PROTECT)
    title = models.CharField( verbose_name="タスク名", max_length=140)
    day_limit = models.DateField(null=True, blank=True, verbose_name="期限日")
    time_limit = models.TimeField(null=True, blank=True, verbose_name="時間の期限")
    memo = models.TextField(null=True, blank=True,  verbose_name="補足情報")
    position = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title