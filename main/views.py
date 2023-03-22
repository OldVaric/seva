from django.shortcuts import render

# Create your views here.

# Это все то что будет на главной странице
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'name': 'Сева',
            'age': '19',
            'car': 'Nissan note e12'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')



