from django import forms
from pybo.models import Question, Answer

# 질문 만들기의 form 검증
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델 (Tb)
        fields = ['subject', 'content'] # 사용 모델(question) 모델의 속성(컬럼)
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        error_messages = {
            'content': {
                'required': "내용을 입력해주세요 #"
            }
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }