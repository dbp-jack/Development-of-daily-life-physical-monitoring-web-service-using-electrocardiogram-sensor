from django import forms
from ecg.models import Duser, Questions
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput
from django.core.exceptions import ValidationError
#회원가입
class SignupForm(UserCreationForm):
    SEX = {
        ('남','남'),
        ('여','여'),
    }
    STATUS = {
        ('Rh-A','Rh-A'),
        ('Rh+A','Rh+A'),
        ('Rh-B','Rh-B'),
        ('Rh+B','Rh-B'),
        ('Rh-O','Rh-O'),
        ('Rh+O','Rh+O'),
        ('Rh-AB','Rh-AB'),
        ('Rh+AB','Rh+AB'),
    }
    sex = forms.ChoiceField(label='성별', choices=SEX, required=True)
    b_type = forms.ChoiceField(label='혈액', choices=STATUS, required=True)
    birth = forms.DateField(label='생년월일', widget=forms.DateInput(attrs={'type': 'date'}))
    height = forms.CharField(label='키(cm)')
    weight = forms.CharField(label='몸무게(kg)')
    class Meta:
        model= Duser
        fields = ('first_name', 'last_name', 'birth', 'username', 'password1', 'password2', 'email', 'sex', 'b_type', 'height', 'weight')

# class QuestionsForm(forms.ModelForm):
#     class Meta:
#         model = Questions
#         fields = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7']
# class CustomRadioSelect(forms.RadioSelect):
#     def render(self, name, value, attrs=None, choices=()):
#         # Only render the radio buttons for 'yes' and 'no' choices
#         final_choices = [(k, v) for k, v in choices if k in ['yes', 'no']]
#         return super().render(name, value, attrs, final_choices)

#class QuestionsForm(forms.ModelForm):
#    class Meta:
#        model = Questions
#        fields = '__all__'
#        widgets = {
#            'question1': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
#            'question2': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
#            'question3': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
#            'question4': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
#            'question5': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
#            'question6': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
#            'question7': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
#        }

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7']
        widgets = {
            'question1': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question2': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question3': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question4': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question5': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question6': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
            'question7': forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
        }