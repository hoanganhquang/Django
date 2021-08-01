from django.shortcuts import render, redirect

from . import util


def index(request):
    if request.method == "POST":
        name = request.POST.get('q')

        return redirect('encyclopedia:md_page', name=name)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def md_page(request, name):
    return render(request, "encyclopedia/md-page.html", {
        "name": util.get_entry(name)
    })


def new_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        util.save_entry(title, content)

        return redirect("encyclopedia:index")

    return render(request, "encyclopedia/new-page.html")
