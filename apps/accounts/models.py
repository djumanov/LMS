from django.db import models
from apps.courses. models import Course


class Teacher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name  = models.CharField(max_length=128)
    phone      = models.CharField(max_length=13)
    profession = models.ManyToManyField(Course, related_name='teachers')
    created_at = models.DateField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name  = models.CharField(max_length=128)
    phone      = models.CharField(max_length=13)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
    

class Parent(models.Model):
    name  = models.CharField(max_length=128)
    phone = models.CharField(max_length=13)
    child = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name