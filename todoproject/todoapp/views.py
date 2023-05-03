from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem

def todoappView(request): #
    return render(request, 'todolist.html')

def todoappView(request): #to store all the todo items
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',{'all_items':all_todo_items}) 

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 