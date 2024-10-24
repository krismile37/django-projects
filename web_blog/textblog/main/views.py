from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Hello', 'World', '123'],
        'obj': {
            'name': 'Tom',
            'age': '27',
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
