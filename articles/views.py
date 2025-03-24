from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) # 사용자의 데이터를 담은 제출 서류
        if form.is_valid():
            form.save()
            return redirect('articles:index')

        # if문이 valied 하지 못했다면 return 값으로 갈 거기 때문에 따로 else를 작성하지 않을 것
    else:
        form = ArticleForm() # html 덩어리 코드가 form에 저장됨

    # context 변수는 if와 else문 밖에 있음
    # if일때도 필요하고 else에서도 사용할 것이기 때문에
    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'detail.html', context)


def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # 앞은 새로운 정보, 뒤는 이전 정보 => 덮어씌워줘
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
        # form = ArticleForm()은 완전히 빈 종이를 만듦, 함수 안 내용은 기존 정보

    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        }
    return render(request, 'update.html', context)


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 기본값은 True, 저장하지말고 일단 대기해봐

            article = Article.objects.get(id=article_id) ## 여기서부터
            comment.article = article
            comment.save() ## 여기까지 뭔소린지 다시 확인해...

            return redirect('articles:detail', id=article_id)
    else:
        return redirect('articles:index') # 처리할 것 없으니까 인덱스로 가아아아ㅏ아ㅏ