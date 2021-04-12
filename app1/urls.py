from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token

from app1 import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api-tokn-auth'),   
    path('task/', views.TaskList.as_view(), name="task_list"),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name="task_detail"),
    path('task-step/', views.TaskStepList.as_view(), name="task_step_list"),
    path('task-step/<int:pk>/', views.TaskStepDetail.as_view(), name="task_step_detail"),
    path('task-file/', views.TaskFileList.as_view(), name="task_file_list"),
    path('task-file/<int:pk>/', views.TaskFileDetail.as_view(), name="task_file_detail"),
    
# <---------------------------FILTER DATA---------------------------------------------------------->
    path('task-list/', views.TaskviewList.as_view(), name="task_view_list"),
    path('task-list/<int:pk>/', views.TaskviewDetail.as_view(), name="task_view_detail"), 
    
#<-------------------------------GROUP----------------------------------------------------->
    path('group/', views.GroupList.as_view(), name="group_list"),
    path('group/<int:pk>/', views.GroupDetail.as_view(), name="group_detail"),
    path('group-task/', views.GroupTaskList.as_view(), name="group_task_list"),
    path('group-task/<int:pk>/', views.GroupTaskDetail.as_view(), name="group_task_detail"),
    path('group-task-step/', views.GroupTaskStepList.as_view(), name="group_task_step_list"),
    path('group-task-step/<int:pk>/', views.GroupTaskStepDetail.as_view(), name="group_task_step_detail"),
    path('group-task-file/', views.GroupTaskFileList.as_view(), name="group_task_file_list"),
    path('group-task-file/<int:pk>/', views.GroupTaskFileDetail.as_view(), name="group_task_file_detail"),
    
# <---------------------------FILTER DATA---------------------------------------------------------->
    path('group-task-list/', views.GroupviewList.as_view(), name="group_view_list"),
    path('group-task-list/<int:pk>/', views.GroupviewDetail.as_view(), name="group_view_detail"), 


#<-------------------------------SHARE------------------------------------------------------------->
    path('task-link/<str:invite_link>/', views.SharedTaskList.as_view()),
    path('task-links/<int:pk>/', views.SharedTaskDetail.as_view()),
    path('group-link/<str:invite_link>/', views.SharedGroupList.as_view()),
    path('group-links/<int:pk>/', views.SharedGroupDetail.as_view()),
    path('group-task-link/<str:invite_link>/', views.SharedGroupTaskList.as_view()),    
    path('group-task-links/<int:pk>/', views.SharedGroupTaskDetails.as_view()),

    path('swagger/', TemplateView.as_view(template_name='index.html'))

]
