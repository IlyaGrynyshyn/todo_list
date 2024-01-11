from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_app.models import Task, Tag


class TodoListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = ["-is_done", "-created"]
    template_name = 'mainapp/index.html'


class TaskCrateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("home")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("home")


class DeleteTaskView(DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("home")


class TaskStatusChangeView(View):
    success_url = reverse_lazy("home")

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(self.success_url)


class TagListView(ListView):
    model = Tag


class TagCrateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")
