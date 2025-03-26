from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # 장고에서 제공하는 User틀을 가져옴, 컬럼 추가하고 싶으면 하단에 추가 가능
    pass