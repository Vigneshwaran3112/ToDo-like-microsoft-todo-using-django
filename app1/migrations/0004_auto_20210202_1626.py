# Generated by Django 3.1.4 on 2021-02-02 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210202_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grouptaskfile',
            old_name='group_task',
            new_name='task',
        ),
        migrations.AddField(
            model_name='grouptaskfile',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.group'),
            preserve_default=False,
        ),
    ]
