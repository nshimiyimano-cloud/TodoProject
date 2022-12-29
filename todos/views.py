from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo

# Create your views here.
def list_todo_items(request):
    context={'todo_list':Todo.objects.all()}
    return render(request,'todos/todo_list.html',context)

def insert_todo_item(request:HttpRequest):
    todo=Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')


def delete_todo_item(request,todo_id):
    todo_to_delete=Todo.objects.get(id=todo_id)
    todo_to_delete.delete()       
    return redirect('/todos/list/')

def update_todo_item(request:HttpRequest,todo_id):
    todo_to_update=Todo.objects.get(id=todo_id)
    if request.method=='POST':
        todo_to_update.content=request.POST['content']
        todo_to_update.save()
        return redirect('/todos/list/')
        
    else:
        return render(request,'todos/edit_item.html',context={'todo_item':todo_to_update})
        





    

