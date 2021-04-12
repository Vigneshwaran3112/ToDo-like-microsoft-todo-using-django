import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import generics
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_class = (IsAuthenticated, )

    def get_object(self):
        return Task.objects.get(pk=self.kwargs['pk'], user=self.request.user)

    def perform_update(self, serializer):
        task = Task.objects.get(pk=self.kwargs['pk'])
        if serializer.validated_data['share']:
            invite_link = str(task.task_uuid)
            if not(TaskShare.objects.filter(invite_link=task.task_uuid)):
                TaskShare.objects.create(user=request.user, task=task, invite_link=invite_link)
        else:
            TaskShare.objects.filter(invite_link=task.task_uuid).delete()
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        Task.objects.filter(pk=kwargs['pk']).update(delete=True)


class TaskStepList(generics.ListCreateAPIView):
    serializer_class = TaskStepSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return TaskStep.objects.filter(user=self.request.user)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)   


class TaskStepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskStep.objects.all()
    serializer_class = TaskStepSerializer
    permission_class = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        TaskStep.objects.filter(pk=kwargs['pk']).update(delete=True)


class TaskFileList(generics.ListCreateAPIView):
    serializer_class = TaskFileSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return TaskFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class TaskFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskFile.objects.all()
    serializer_class = TaskFileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    permission_class = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        TaskFile.objects.filter(pk=kwargs['pk']).update(delete=True)


#<----------------------------------------GROUP-------------------------------------------------------->

class GroupList(generics.ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_class = (IsAuthenticated, )
    
    def get_object(self):
        return Group.objects.get(pk=self.kwargs['pk'], user=self.request.user)

    def perform_update(self, serializer):
        group = Group.objects.get(pk=self.kwargs['pk'])
        if serializer.validated_data['share']:
            invite_link = str(group.group_uuid)
            if not(GroupShare.objects.filter(invite_link=group.group_uuid)):
                GroupShare.objects.create(user=request.user, group=group, invite_link=invite_link)
        else:
            GroupShare.objects.filter(invite_link=group.group_uuid).delete()
        serializer.save()   

    def destroy(self, request, *args, **kwargs):
        Group.objects.filter(pk=kwargs['pk']).update(delete=True)


class GroupTaskList(generics.ListCreateAPIView):
    permission_class = (IsAuthenticated, )
    serializer_class = GroupTaskSerializer

    def get_queryset(self):
        return GroupTask.objects.filter(user=self.request.user.id, delete=False, status=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupTaskSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return GroupTask.objects.filter(user=self.request.user.id, delete=False, status=True)

    def perform_update(self, serializer):
        group_task = GroupTask.objects.get(pk=pk)
        if serializer.validated_data['share']:
            invite_link = str(group_task.group_task_uuid)
            if not(GroupTaskShare.objects.filter(invite_link=group_task.group_task_uuid)):
                GroupTaskShare.objects.create(user=request.user, group_task=group_task, invite_link=invite_link)
        else:
            GroupTaskShare.objects.filter(invite_link=group_task.group_task_uuid).delete()

        serializer.save()    

    def destroy(self, request, *args, **kwargs):
        GroupTask.objects.filter(pk=kwargs['pk']).update(delete=True)


class GroupTaskStepList(generics.ListCreateAPIView):
    serializer_class = GroupTaskStepSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return GroupTaskStep.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class GroupTaskStepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupTaskStep.objects.all()
    serializer_class = GroupTaskStepSerializer
    permission_class = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        GroupTaskStep.objects.filter(pk=kwargs['pk']).update(delete=True)


class GroupTaskFileList(generics.ListCreateAPIView):
    serializer_class = GroupTaskFileSerializer
    parser_classes = [parsers.MultiPartParser]
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return GroupTaskFile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupTaskFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupTaskFile.objects.all()
    serializer_class = GroupTaskFileSerializer
    permission_class = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        groupTaskFile.objects.filter(pk=kwargs['pk']).update(delete=True)

# <--------------------------------------------- FILTER DATA ----------------------------------------------->

class TaskviewList(generics.ListAPIView):
    serializer_class = TaskListSerializer
    parser_classes = [parsers.MultiPartParser]
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.id, delete=False, status=True)

class TaskviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.id, delete=False, status=True)


class GroupviewList(generics.ListAPIView):
    serializer_class = GroupTaskListSerializer
    parser_classes = [parsers.MultiPartParser]
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user.id, delete=False, status=True)


class GroupviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupTaskListSerializer
    parser_classes = [parsers.MultiPartParser]
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return Group.objects.filter(pk=self.kwargs['pk'], user=self.request.user.id, delete=False, status=True)

# <--------------------------------------------- TASK & GROUP SHARE----------------------------------------------->\

class SharedTaskList(generics.ListAPIView):
    serializer_class = TaskShareSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        shared = TaskShare.objects.get(invite_link=self.kwargs['invite_link'], delete=False, status=True)
        Task.objects.filter(pk=shared.task.pk).shared_users.add(self.request.user)
        return TaskShare.objects.filter(invite_link=self.kwargs['invite_link'])


class SharedTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskShareSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    permission_class = (IsAuthenticated, )

    def retrieve(self, request, pk):
        shared_task = TaskShare.objects.get(pk=pk, user=self.request.user.id, delete=False, status=True)
        return Response (TaskListSerializer(Task.objects.get(pk=shared_task.task.pk)).data)

    def update(self, request, pk):
        shared_task = TaskShare.objects.get(pk=pk, user=self.request.user.id, delete=False, status=True)
        serializer = TaskListSerializer(Task.objects.get(pk=shared_task.task.pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SharedGroupTaskList(generics.ListAPIView):
    serializer_class = GroupTaskShareSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return GroupTaskShare.objects.filter(invite_link=self.kwargs['invite_link'])


class SharedGroupTaskDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupTaskShareSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    permission_class = (IsAuthenticated, )

    def retrieve(self, request, pk):
        shared_group_task = GroupTaskShare.objects.get(pk=pk, user=self.request.user.id, delete=False, status=True)
        return Response (GroupTaskSerializer(GroupTask.objects.get(pk=shared_group_task.group_task.pk)).data)

    def update(self, request, pk):
        shared_group_task = GroupTaskShare.objects.get(pk=pk, user=self.request.user.id, delete=False, status=True)
        serializer = GroupTaskSerializer(GroupTask.objects.get(pk=shared_group_task.group_task.pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class SharedGroupList(generics.ListAPIView):
    serializer_class = GroupShareSerializer
    permission_class = (IsAuthenticated, )

    def get_queryset(self):
        return GroupShare.objects.filter(invite_link=self.kwargs['invite_link'])


class SharedGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupShareSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    permission_class = (IsAuthenticated, )

    def retrieve(self, request, pk):
        shared_group = GroupShare.objects.get(pk=pk, user=self.request.user.id, delete=False, status=True)
        return Response (GroupTaskListSerializer(GroupTask.objects.get(pk=shared_group.group.pk)).data)

    def update(self, request, pk):
        shared_group = GroupShare.objects.get(pk=pk, user=self.request.user.id, delete=False, status=True)
        serializer = GroupTaskListSerializer(GroupTask.objects.get(pk=shared_group.group.pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)