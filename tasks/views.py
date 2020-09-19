from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.shortcuts import redirect
# from django.contrib.sessions.models import Session
# from django.contrib.auth.models import User

def todo_view(request):
    all_todo_items = TodoItem.objects.filter(username=request.user)
    user = request.user
    return render(request, 'todo.html',
        {'all_items': all_todo_items})


def add_todo(request):
    new_item = TodoItem(content = request.POST['content'],username=request.user)
    new_item.save()
    return HttpResponseRedirect('/tasks')

def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/tasks')


        
