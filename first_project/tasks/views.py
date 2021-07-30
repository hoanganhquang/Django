from django.shortcuts import render

# Create your views here.

tasks = ["1", "2", "3"]


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add_task(request):
    return render(request, "tasks/add.html")
