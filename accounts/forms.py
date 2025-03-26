from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        # fields = '__all__'
        fields = ('username', ) 

class CustomAuthenticationForm(AuthenticationForm):
    # 인증 페이지의 폼도 id/pw 외에 mail/pw 등 다양한 인증 수단을 추가할 수 있으므로 폼을 확장
    pass
    