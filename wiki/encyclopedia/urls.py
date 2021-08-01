from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.md_page, name="md_page"),
    path("/newpage", views.new_page, name="new_page"),
    path("<str:name>/editpage", views.edit_page, name="edit_page"),
    path("/randompage", views.random_page, name="random_page")
]
