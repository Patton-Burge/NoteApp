from django.shortcuts import render, redirect
from random import randint
from .models import Note


def home(request):
    number0 = randint(10, 25)
    number1 = randint(10, 25)
    number2 = randint(10, 25)
    return render(
        request,
        "home.html",
        {"number0": number0, "number1": number1, "number2": number2},
    )


def submit_note(request):
    title = request.POST["title"]
    content = request.POST["content"]
    note = Note.objects.all()
    note.create(
        title=title, content=content
    )
    return redirect("home")
