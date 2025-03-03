from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View 
from .models import Task
from .forms import TodoForm
#to dealing with ajax
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
def home(request):
    return render(request,'base.html',{'title':'Nex'})

class TodoList(View):
    def get(self, request):
        form = TodoForm()
        tasks = Task.objects.all()
        context = {
            'title': 'List',
            'form': form,
            'tasks': tasks,
        }
        return render(request,'todo/todo_list.html',context)

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            #return redirect('todos-list')
            return JsonResponse({'task':model_to_dict(new_task)}, status=200)
        else:
            return redirect('todos-list')
class TodoCompleted(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        if task :
            task.done = True
            task.save()
            return JsonResponse({'task':model_to_dict(task)}, status=200)
class TodoDeleted(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        if task :
            task.delete()
            print(task,'deleted: OK')
            return JsonResponse({'result': 'ok'}, status=200)