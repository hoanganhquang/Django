from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def css_page(request, name):
    return render(request, "encyclopedia/csspage.html", {
        "name": util.get_entry(name)
    })
