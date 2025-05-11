from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class Duser(AbstractUser):
    sex = models.CharField(max_length=20, null=True)
    b_type = models.CharField(max_length=30, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)

class Questions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    question1 = models.BooleanField(default=False, verbose_name='턱, 목 또는 등쪽에 통증이나 불편함이 있다.')
    question2 = models.BooleanField(default=False, verbose_name='가족중 고혈압이나 심장병이 있다.')
    question3 = models.BooleanField(default=False, verbose_name='가슴에 통증이나 불편감이 있다.')
    question4 = models.BooleanField(default=False, verbose_name='숨이 찬다.')
    question5 = models.BooleanField(default=False, verbose_name='힘이 없고, 어지럽다.')
    question6 = models.BooleanField(default=False, verbose_name='한쪽 또는 양쪽 눈이 흐리게 보인다.')
    question7 = models.BooleanField(default=False, verbose_name='팔 또는 어깨에 통증이나 불편감이 있다.')
    total = models.IntegerField(default=0, editable=False)
    status = models.CharField(max_length=20, default='')
    u_id = models.ForeignKey(Duser, on_delete=models.CASCADE)

class ChartData(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} at {self.timestamp}"
    
class Avg(models.Model):
    avg = models.FloatField(default=0)
    status = models.CharField(max_length=20, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    u_id = models.ForeignKey(Duser, on_delete=models.CASCADE)
