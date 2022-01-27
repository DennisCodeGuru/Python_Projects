from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    Title = models.TextField(max_length=60, default="", null=True)
    Course_Number = models.IntegerField(default=000)
    Instructor_Name = models.TextField(max_length=60, default="")
    Duration = models.FloatField(default=000, max_length=60, null=True)



    objects = models.Manager()

    def __str__(self):
        return self.Title

class1 = djangoClasses(Title='HTML',Course_Number=101,Instructor_Name='Mr Jones',Duration=1)
class1.save()

class2 = djangoClasses(Title='JavaSkript',Course_Number=327,Instructor_Name='Mr Jones',Duration=2)
class2.save()

class3 = djangoClasses(Title='Python',Course_Number=216,Instructor_Name='Mr Jones',Duration=3)
class3.save()