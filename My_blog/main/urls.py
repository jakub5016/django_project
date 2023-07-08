from django.urls import path
from . import views


urlpatterns = [
    path("<int:id>", views.list, name="list"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
]