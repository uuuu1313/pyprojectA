from django.urls import path

from pybo import views

urlpatterns = [
    path('', views.index), # pybo/ url은 pybo.views의 index 함수에 정의함
    path('<int:question_id>/', views.detail), # question 게시글 상세 보기는 views의 detail함수에 정의
]