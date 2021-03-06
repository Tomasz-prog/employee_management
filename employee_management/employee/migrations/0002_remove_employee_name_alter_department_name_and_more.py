# Generated by Django 4.0.3 on 2022-03-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='usercode',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='operations',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
