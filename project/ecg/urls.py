from django.urls import path
from . import views
from .views import (Questions_view, dis_information_view, RecordView, UserDetailView)

app_name = "ecg"
urlpatterns = [
    path('login/', views.Login, name="login"), # 로그인 URL
    path('logout/', views.Logout, name="logout"), # 로그아웃
    path('signup/', views.Signup, name="signup"), # 회원가입 URL
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),
    path('chart/', views.chart_view, name='chart_view'),
    path('record/', RecordView.as_view(), name='record'),
    path('dis_information/', dis_information_view, name='dis_information'),
    path('inform/', UserDetailView.as_view(), name='inform'),
    path('questions/', Questions_view, name='questions'),
]