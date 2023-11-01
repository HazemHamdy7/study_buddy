from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets Learn Python!'},
    {'id': 2, 'name': 'Design with me !'},
    {'id': 3, 'name': 'Frondend developers!'},
]


def home(requset):
    return render(requset, 'home.html', {'rooms': rooms})


def room(requset):
    return render(requset, 'room.html')
