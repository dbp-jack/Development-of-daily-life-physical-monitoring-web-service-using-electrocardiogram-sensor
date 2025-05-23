from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, QuestionsForm
from .models import Duser, Questions, ChartData, Avg
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import DetailView, ListView
from datetime import datetime
from pytz import timezone
from django.views.decorators.csrf import csrf_exempt
#회원가입
def Signup(request):
    if request.method == "GET":
        signupForm = SignupForm()
        context = {'signupForm': signupForm}
        return render(request, 'ecg/signup.html', context)
    
    elif request.method == "POST":
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            duser = signupForm.save(commit=False)
            duser.save()
            # Redirect to the login page upon successful registration
            return redirect("ecg:login")
        else:
            # If registration fails, return the form with errors
            return render(request, 'ecg/signup.html', {'signupForm': signupForm})
#로그인
def Login(request):
    if request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            print("인증성공")
            auth_login(request, loginForm.get_user())
            return redirect("ecg:chart_view")
        else:
            print("인증실패")
            return render(request, 'ecg/login.html', {'error': '로그인 실패'})
    return render(request, 'ecg/login.html')

#로그아웃
def Logout(request):
    user = request.user.username
    auth_logout(request)
    return redirect("ecg:login")

#회원정보
class UserDetailView(LoginRequiredMixin, DetailView):
    model = Duser
    template_name = 'ecg/inform_detail.html'
    context_object_name = 'user'
    
    def get_object(self, queryset=None):
        return self.request.user

# 동적 차트

@login_required
def get_chart_data(request):
    start_time_str = request.GET.get('start_time')
    if not start_time_str:
        return JsonResponse({'data': []})

    try:
        start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        start_time = start_time.replace(tzinfo=timezone('UTC'))
    except ValueError:
        return JsonResponse({'data': [], 'error': 'Invalid timestamp format'})

    data = ChartData.objects.filter(timestamp__gte=start_time).order_by('timestamp')
    data_values = [item.value for item in data]
    return JsonResponse({'data': data_values})

@login_required
def chart_view(request):
    if request.method == 'POST':
        avg_value = float(request.POST.get('avg_value'))
        status = request.POST.get('status')
        new_avg = Avg(avg=avg_value, status=status, u_id=request.user)
        new_avg.save()
        return JsonResponse({'status': 'success'})
    return render(request, 'ecg/chart.html')

#건강체크
@login_required
def Questions_view(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            # Calculate the total based on the selected 'yes' answers
            total = sum([int(getattr(instance, f)) for f in form.Meta.fields if getattr(instance, f)])
            instance.total = total
            instance.u_id = request.user

            # Conditional statements based on the total value
            if total == 0:
                instance.status = '양호'
                result_message = "지금 현재 양호한 상태입니다。"
            elif total >= 3 and total <=5 :
                instance.status = '주의'
                result_message = "건강 상태가 좋지 않습니다。 가까운 병원에 방문하시길 바랍니다。"
            elif total > 5:
                instance.status = '심각'
                result_message = "지금 즉시 응급실로 연락하시길 바랍니다。"
            else:
                instance.status = '양호'
                result_message = "지금 현재 양호한 상태입니다。"

            instance.save()

            return render(request, 'ecg/questions.html', {'form': form, 'questions': Questions.objects.filter(u_id=request.user), 'result_message': result_message})

    else:
        form = QuestionsForm()
        result_message = ""

    questions = Questions.objects.filter(u_id=request.user)
    return render(request, 'ecg/questions.html', {'form': form, 'questions': questions, 'result_message': result_message})

# 건강기록
class RecordView(LoginRequiredMixin, ListView):
    model = Avg
    template_name = 'ecg/record.html'
    context_object_name = 'record'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_avgs'] = Avg.objects.filter(u_id=self.request.user).order_by('timestamp')
        context['all_questions'] = Questions.objects.filter(u_id=self.request.user).order_by('id')
        return context
    
# 질병 및 질환 정보
def dis_information_view(request):
    return render(request, 'ecg/dis_information.html')