from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 기본 필드 외에 추가하고 싶은 필드를 정의합니다
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    
    # 필요한 경우 USERNAME_FIELD를 변경할 수 있습니다
    # USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.username
