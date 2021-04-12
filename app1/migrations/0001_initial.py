# Generated by Django 3.1.4 on 2021-01-29 15:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('task', models.CharField(max_length=100)),
                ('myday', models.BooleanField(default=False)),
                ('starred', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('remind', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Due Date')),
                ('repeat', models.IntegerField(choices=[(1, 'DAILY'), (2, 'WEEKLY'), (3, 'MONTHLY'), (4, 'YEARLY')], null=True)),
                ('addnotes', models.TextField(blank=True, max_length=300)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('task', models.CharField(max_length=100)),
                ('myday', models.BooleanField(default=False)),
                ('starred', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('remind', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Due Date')),
                ('repeat', models.IntegerField(choices=[(1, 'DAILY'), (2, 'WEEKLY'), (3, 'MONTHLY'), (4, 'YEARLY')], null=True)),
                ('addnotes', models.TextField(blank=True, max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('steps', models.CharField(max_length=30)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_step', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('invite_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_share', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='files/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_file', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupTaskStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('steps', models.CharField(max_length=30)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.group')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.grouptask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group_step', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupTaskShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('invite_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('grouptask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.grouptask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group_task_share', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupTaskFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='files/')),
                ('group_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.grouptask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group_file', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('invite_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group_share', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
