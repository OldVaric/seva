from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'), #Это отображение главной старницы
    path('about', views.about, name='about'),
]