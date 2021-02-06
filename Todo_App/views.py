from django.shortcuts import render, redirect
from Todo_App.models import Todo
from Todo_App.forms import TodoForm


# Create your views here.
def home(request):
    """It will display all Todos(records) & create a new record(todos)"""
    if request.method == "POST":
        todo_create = TodoForm(request.POST)
        if todo_create.is_valid():
            todo_create.save()
        return redirect('home')
    else:
        # it will fetch all records in the database
        todos = Todo.objects.all()
        # creating an object of TodoForm(TodoModel)
        create_todo = TodoForm()
        context   = {
            'todos': todos,
            'create_todo': create_todo,
        }
        return render(request, 'index.html', context)


def update(request, pk):
    """it will update the selected record (selected_todo)"""
    current_todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        update_todo = TodoForm(request.POST, instance=current_todo)
        if update_todo.is_valid():
            update_todo.save()
        return redirect('home')
    else:
        update_todo = TodoForm(instance=current_todo)
        context     = {'update_todo': update_todo}
        return render(request, 'update.html', context)


def delete(request, pk):
    """it will delete the selected record """
    current_todo = Todo.objects.get(id=pk)
    current_todo.delete()
    return redirect('home')
