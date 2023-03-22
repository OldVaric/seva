
from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsView.as_view(), name='news_home'), #Это отображение новостей или статей старницы
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDV.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUV.as_view(), name='news-update'),
    path('search/', views.Search.as_view(), name='search'),
]