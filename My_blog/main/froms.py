from django import forms
from .models import ToDoList

class createNewList(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('name', )

        widget ={
            'class': 'form-control rounded-pill w-25 bg-dark' , 'style' :'margin-bottom: 10px;margin-top: 10px; font-family:Arial;'
        }
