from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .froms import createNewList
# Create your views here.

all_lists = ToDoList.objects.all()

def list(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method =="POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.compile = True
                else:
                    item.compile = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, compile=False)
            else:
                print("INVALID")
    

    return render(response, "main/list.html", {"ls":ls, "all_lists" : all_lists})


def home(response):
    return render(response, "main/home.html", {"all_lists" : all_lists})

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
    return render(response, "main/create.html", {"form":formula, "all_lists" : all_lists})

def index(response):
    return render(response, "main/index.html", {"all_lists" : all_lists})