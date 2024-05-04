from django.apps import AppConfig


class PyboConfig(AppConfig): # DB 생성시 해당 클래스를 config/setting.py 의 INSTALLED_APPS에 추가하기!
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'
