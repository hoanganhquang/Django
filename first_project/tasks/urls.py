from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("task", add_task, name="add_task")
]
