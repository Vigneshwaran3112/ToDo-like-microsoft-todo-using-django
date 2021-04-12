import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    pass


class BaseModel(models.Model):
    delete = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseTaskModel(BaseModel):
    
    repeat_mode = (
        (1, "DAILY"),
        (2, "WEEKLY"),
        (3, "MONTHLY"),
        (4, "YEARLY"),
    )

    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_tasks', null=True, blank=True)
    task = models.CharField(max_length=100)
    myday = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    remind = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True, verbose_name='Due Date')
    repeat = models.IntegerField(choices=repeat_mode, null=True)
    addnotes = models.TextField(max_length=300, blank=True)
    share = models.BooleanField(default=False)
    shared_users = models.ManyToManyField(BaseUser, blank=True)

    class Meta:
        abstract = True


class Task(BaseTaskModel):
    task_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return self.task


class TaskStep(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_step',  null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='user_task')
    steps = models.CharField(max_length=30)

    def __str__(self):
        return self.steps


class TaskFile(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_file', null=True, blank=True)
    task = models.ForeignKey(Task, on_delete = models.CASCADE, related_name='user_task_file')
    file = models.FileField(upload_to ='files/') 

    def __str__(self):
        return f'{self.user.username}-{self.task.task}-file'


class TaskShare(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_share', null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_to_share')
    invite_link = models.CharField(max_length=255, verbose_name='invite link')
  

#<--------------------------------------------GROUP-------------------------------------------------------->

class Group(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_groups', null=True, blank=True)
    group_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    share = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class GroupTask(BaseTaskModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='user_groups')
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='group_user', null=True, blank=True)
    group_task_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.task


class GroupTaskStep(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_group_step', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name='group_step')
    task = models.ForeignKey(GroupTask, on_delete=models.CASCADE, related_name='group_task_step')
    steps = models.CharField(max_length=30)

    def __str__(self):
        return self.steps


class GroupTaskFile(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_group_file', null=True, blank=True)
    task = models.ForeignKey(GroupTask, on_delete=models.CASCADE, related_name='group_task_file')
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name='group_file')
    file = models.FileField(upload_to ='files/') 

    def __str__(self):
        return f'{self.user.username}-{self.task.task}-file'


class GroupShare(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_group_share', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_share')
    invite_link = models.CharField(max_length=255, verbose_name='invite link')
    

class GroupTaskShare(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_group_task_share', null=True, blank=True)
    group_task = models.ForeignKey(GroupTask, on_delete = models.CASCADE, related_name='group_task_share')
    invite_link = models.CharField(max_length=255, verbose_name='invite link')
