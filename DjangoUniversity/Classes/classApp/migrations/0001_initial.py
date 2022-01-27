# Generated by Django 4.0.1 on 2022-01-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Django',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
                ('Title', models.TextField(blank=True, default='', max_length=60)),
                ('Course_Number', models.IntegerField(default=0, max_length=60)),
                ('Instructor_Name', models.TextField(blank=True, default='', max_length=60)),
                ('Duration', models.FloatField(default=0, max_length=60)),
            ],
        ),
    ]
