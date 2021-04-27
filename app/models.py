from django.db import models
from django.urls import reverse
# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=50)
    principal=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})


class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(school,related_name="students",on_delete=models.SET_DEFAULT,default=1)
    def __str__(self):
        return self.name
