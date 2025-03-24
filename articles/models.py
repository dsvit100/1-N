from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comment_set = 자동으로 저장됨


class Comment(models.Model):
    content = models.TextField()
    # 두 클래스를 foreingkey 관계로 묶어줌
    # on_delete는 필수인자 = 부모가 지워졌을 때, 를 의미
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # models.CASCADE는 부모 내용이 지워지면 컨텐츠도 지워주세요
    # 나보다 한단계 위에 있는 모델
    # 모델을 새로 만들었으면 번역본 만드는 코드(migration)r를 다시 쳐줘야 함
    # article_id = 자동으로 저장됨