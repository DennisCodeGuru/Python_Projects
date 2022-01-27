from django.db import models

# Create your models here.
class Django(models.Model):
    Title = models.TextField(max_length=60, default="", null=True)
    Course_Number = models.IntegerField(default=000, max_length=60)
    Instructor_Name = models.TextField(max_length=60, default="")
    Duration = models.FloatField(default=000, max_length=60, null=True)



    objects = models.Manager()

    def __str__(self):
        return self.Title
