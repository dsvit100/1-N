from django.forms import ModelForm
from django import forms
from .models import Article, Comment

class ArticleForm(ModelForm):
# 기능 완성 후 꾸며주기 위해 기존에 사용한 Article 모델의 title을 덮어씌워줌
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    class Meta():
        model = Article
        fields = '__all__'
        # input title, input content 대신 사용함
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }


# comment폼 만들기
class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # fields = '__all__'

        # fields => 추가할 필드 목록
        # fields = ('content', ) # fields에 title과 content 둘 다 있지만 나는 content만 입력을 받을거야 (선택)
        # esclude => 제외할 필드 목록
        exclude = ('article', ) # fields에 title과 content 둘 다 있지만 'article'을 제외해주세요