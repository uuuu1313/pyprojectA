from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): # UserCreateionForm 을 상속함
    email = forms.EmailField(label="이메일", error_messages={'required':'이메일 입력@'}) # 필드를 추가하기 위해서는 상속을 해야함
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        error_messages = {
            'email': {
                'required': "비밀번호를 입력해주세요 #"  # 에러 메시지 설정
            }
        }