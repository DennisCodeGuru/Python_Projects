# Generated by Django 4.0.1 on 2022-01-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='django',
            name='type',
        ),
        migrations.AlterField(
            model_name='django',
            name='Duration',
            field=models.FloatField(default=0, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='django',
            name='Instructor_Name',
            field=models.TextField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='django',
            name='Title',
            field=models.TextField(default='', max_length=60, null=True),
        ),
    ]
