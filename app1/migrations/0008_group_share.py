# Generated by Django 3.1.4 on 2021-02-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210203_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='share',
            field=models.BooleanField(default=False),
        ),
    ]
