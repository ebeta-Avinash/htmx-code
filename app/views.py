from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()

    is_active_filter = request.GET.get('is_active', None)
    if is_active_filter:
        tasks = tasks.filter(is_active=is_active_filter)

    search_query = request.GET.get('search', None)
    if search_query:
        tasks = tasks.filter(title__icontains=search_query) | tasks.filter(description__icontains=search_query)

    return render(request, 'app/index.html', {'tasks': tasks})



def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(title=title, description=description)

        return redirect('task-list')

    return redirect('task-list')


def deactivate_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    task.is_active = not task.is_active
    task.save()

    return redirect('task-list')


def delete_task(request, pk):
    Task.objects.get(id=pk).delete()
    tasks = Task.objects.all()
    return render(request, 'app/index.html', {'tasks': tasks})