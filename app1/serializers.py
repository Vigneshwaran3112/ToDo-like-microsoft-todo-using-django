from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import *


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        created_user = BaseUser.objects.create_user(**validated_data, is_staff=True, is_superuser=True)
        token, created = Token.objects.get_or_create(user=created_user)
        return {'username': created_user.username, 'email': created_user.email, 'token': token.key}

    def to_representation(self, instance):
        return {
            'username': instance.username,
            'email': instance.email
        }


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):     
        return {
            "user": instance.user.id,
            "id": instance.pk,
            "task": instance.task,
            "addsteps": TaskStepSerializer(TaskStep.objects.filter(task=instance.id).order_by('id'), many=True).data,
            "myday": instance.myday,
            "starred": instance.starred,
            "completed": instance.completed,
            "remind": instance.remind.strftime('%d/%m/%Y') if instance.remind else None,
            "due_date": instance.due_date.strftime('%d/%m/%Y') if instance.due_date else None,
            "repeat": instance.repeat,
            "addfile": TaskFileSerializer(TaskFile.objects.filter(task=instance.id).order_by('id'), many=True).data,
            "addnotes": instance.addnotes,
            "delete": instance.delete,
            "status": instance.status,
            "created": instance.created,
            "updated": instance.updated,
            "share": instance.share
        }


class TaskStepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskStep
        fields = '__all__'


class TaskFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskFile
        fields = '__all__'

    
class TaskShareSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskShare
        fields = '__all__'


    def to_representation(self, instance):
        return { 
            "id": instance.id,
            "invite_link": instance.invite_link,
            "user": BaseUserSerializer(BaseUser.objects.get(pk=instance.user.pk)).data,
            "task": TaskListSerializer(Task.objects.get(task_uuid=instance.invite_link)).data
         }

#<------------------------------------------GROUP----------------------------------------------------->

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'


class GroupTaskSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = GroupTask
        fields = '__all__'

    def to_representation(self, instance):          
        return {
            "user": instance.user.id,
            "id": instance.id,
            "group_task_uuid": instance.group_task_uuid,
            "group": instance.group.id,
            "task": instance.task,
            "steps": GroupTaskStepSerializer(GroupTaskStep.objects.filter(user=instance.user.id, group=instance.group.id, task=instance.id).order_by('id'), many=True).data,
            "myday": instance.myday,
            "starred": instance.starred,
            "completed": instance.completed,
            "remind": instance.remind.strftime('%d/%m/%Y') if instance.remind else None,
            "due_date": instance.due_date.strftime('%d/%m/%Y') if instance.due_date else None,
            "repeat": instance.repeat,
            "addnotes": instance.addnotes,
            "addfiles": GroupTaskFileSerializer(GroupTaskFile.objects.filter(user=instance.user.id, group=instance.group.id, task=instance.id).order_by('id'), many=True).data,
            "delete": instance.delete,
            "status": instance.status,
            "created": instance.created,
            "updated": instance.updated,
            "share": instance.share
        }   


class GroupTaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupTask
        fields = ('user', 'id', 'group')

    def to_representation(self, instance):
        return {
            "user": instance.user.id,
            "id": instance.id,
            "group": instance.id,
            "task": GroupTaskSerializer(GroupTask.objects.filter(user=instance.user.id, group=instance.id).order_by('id'), many=True).data
        }


class GroupTaskStepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GroupTaskStep
        fields = '__all__'

class GroupTaskFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GroupTaskFile
        fields = '__all__'

    
class GroupShareSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GroupShare
        fields = '__all__'

    def to_representation(self, instance):
        return { 
            "id": instance.id,
            "invite_link": instance.invite_link,
            "user": BaseUserSerializer(BaseUser.objects.get(pk=instance.user.pk)).data,
            "Group": GroupTaskListSerializer(Group.objects.get(group_uuid=instance.invite_link)).data
         }

    
class GroupTaskShareSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GroupTaskShare
        fields = '__all__'

    def to_representation(self, instance):
        return { 
            "id": instance.id,
            "invite_link": instance.invite_link,
            "user": BaseUserSerializer(BaseUser.objects.get(pk=instance.user.pk)).data,
            "group_task": GroupTaskSerializer(GroupTask.objects.get(group_task_uuid=instance.invite_link)).data
         }