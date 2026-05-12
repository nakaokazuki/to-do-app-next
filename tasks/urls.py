from django.urls import path

from . import views


urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("toggle/<int:pk>/", views.toggle_task, name="toggle_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("edit/<int:pk>/", views.task_edit, name="task_edit"),
    path("", views.task_list, name="task_list"),
    path("bulk-delete/", views.task_bulk_delete, name="task_bulk_delete"),
    path("toggle/<int:pk>/", views.toggle_task, name="toggle_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("edit/<int:pk>/", views.task_edit, name="task_edit"),
    path("<int:pk>/", views.task_detail, name="task_detail"),
]