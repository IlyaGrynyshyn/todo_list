from django.urls import path, include
from todo_app.views import TodoListView, TaskCrateView, TaskUpdateView, DeleteTaskView, TaskStatusChangeView, \
    TagListView, TagCrateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create-task/", TaskCrateView.as_view(), name="create-task"),
    path("update-task/<int:pk>/", TaskUpdateView.as_view(), name="update-task"),
    path("delete-task/<int:pk>/", DeleteTaskView.as_view(), name="delete-task"),
    path("change-status/<int:pk>/", TaskStatusChangeView.as_view(), name="change-status"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("create-tag/", TagCrateView.as_view(), name="create-tag"),
    path("delete-tag/<int:pk>/", TagDeleteView.as_view(), name="delete-tag"),
    path("update-tag/<int:pk>/", TagUpdateView.as_view(), name="update-tag")
]
