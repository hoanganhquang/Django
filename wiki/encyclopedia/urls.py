from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.md_page, name="md_page"),
    path("/newpage", views.new_page, name="new_page")
]
