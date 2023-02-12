from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница!!!',
        'values': ['some', 'hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 20,
            'hobby': 'golf',
        }
    }
    return render(request,'newsite/index.html', data)


def about(request):
    return render(request,'newsite/about.html')