# Generated by Django 4.0.1 on 2022-01-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0002_remove_django_type_alter_django_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(default='', max_length=60, null=True)),
                ('Course_Number', models.IntegerField(default=0)),
                ('Instructor_Name', models.TextField(default='', max_length=60)),
                ('Duration', models.FloatField(default=0, max_length=60, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Django',
        ),
    ]
