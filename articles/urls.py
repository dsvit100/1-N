from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # Create
    path('create/', views.create, name='create'),

    # read
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    # Update
    path('<int:id>/update/', views.update, name='update'),

    # Delete
    path('<int:id>/delete/', views.delete, name='delete'),


    # Comment
    # Create
    # int:article_id = 변수의 이름을 지정해 주는 것, 값을 가져오는 것이 아님
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),

    # Delete
    path('<int:article_id>/comments/<int:id>/delete', views.comment_delete, name='comment_delete'),
]