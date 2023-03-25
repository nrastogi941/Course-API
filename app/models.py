from django.db import models

class CourseModel(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    discount=models.IntegerField(default=0)
    description=models.FloatField()
