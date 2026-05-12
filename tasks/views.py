from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import Task


def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    tasks = Task.objects.order_by("-created_at")
    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks, "form": form},
    )


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("task_list")


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_list")


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "task": task},
    )