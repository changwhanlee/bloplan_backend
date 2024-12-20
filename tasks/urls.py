from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view()),
    path('test', views.TaskTest.as_view()),
    path('total', views.TaskTotalView.as_view()),
    path('date-update', views.TaskDateUpdateView.as_view()),
    path('platforms', views.PlatformListView.as_view()),
    path('platforms/add', views.AddPlatformView.as_view()),
    path('<int:pk>', views.TaskDetailView.as_view()),
    path('<int:pk>/status', views.TaskStatusUpdateView.as_view()),
    path('<int:pk>/modify', views.ModifyTaskView.as_view()),
    path('<int:pk>/delete', views.DeleteTaskView.as_view()),
]
