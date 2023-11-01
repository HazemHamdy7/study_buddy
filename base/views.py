from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets Learn Python!'},
    {'id': 2, 'name': 'Design with me !'},
    {'id': 3, 'name': 'Frondend developers!'},
]


def home(requset):
    context = {'rooms': rooms}
    return render(requset, 'base/home.html', context)


def room(requset, pk):

    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(requset, 'base/room.html', context)
