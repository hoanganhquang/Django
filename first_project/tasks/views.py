from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add_task(request):
    if request.method == "POST":
        task = request.POST.dict()
        task = task.get("task")
        request.session["tasks"] += [task]

        return redirect('tasks:index')

    return render(request, "tasks/add.html")
