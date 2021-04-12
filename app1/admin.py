from django.contrib import admin
from .models import *


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task', 'share')
    list_display_links = ('id', 'task', 'share')


@admin.register(TaskStep)
class TaskStepAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task')
    list_display_links = ('id', 'task')


@admin.register(TaskFile)
class TaskFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task')
    list_display_links = ('id', 'task')


@admin.register(TaskShare)
class TaskShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task', 'invite_link')
    list_display_links = ('id', 'task', 'invite_link')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'share')
    list_display_links = ('id', 'user', 'name', 'share')


@admin.register(GroupTask)
class GroupTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group')
    list_display_links = ('id', 'group')


@admin.register(GroupTaskStep)
class GroupTaskStepAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'task')
    list_display_links = ('id', 'group', 'task')


@admin.register(GroupTaskFile)
class GroupTaskFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'task')
    list_display_links = ('id', 'group', 'task')


@admin.register(GroupShare)
class GroupShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'invite_link')
    list_display_links = ('id', 'user', 'group')


@admin.register(GroupTaskShare)
class GroupTaskShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group_task', 'invite_link')
    list_display_links = ('id', 'user', 'group_task')
