from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .froms import createNewList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls" :ls})


def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        formula = createNewList(response.POST)

        if formula.is_valid():
            name = formula.cleaned_data["name"]
            t = ToDoList(name=name)
            t.save()

        return HttpResponseRedirect("/%i" %t.id) 
    else:
        formula = createNewList()
    return render(response, "main/create.html", {"form":formula})