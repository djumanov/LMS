from django.db import models
from apps.courses. models import Course


class Teacher(models.Model):
    type_choices = [
        ('main', 'Main'),
        ('ass', 'Assistent'),
    ]
    first_name = models.CharField(max_length=128)
    last_name  = models.CharField(max_length=128)
    phone      = models.CharField(max_length=13)
    profession = models.ManyToManyField(Course, related_name='teachers')
    type       = models.CharField(max_length=4, choices=type_choices, default='main')
    created_at = models.DateField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
    

class Student(models.Model):
    choices = (
        ('z', 'zero'),
        ('s', 'studying'),
        ('p', 'pause'),
        ('d', 'drop out'),
        ('g', 'graduated'),
    )
    first_name = models.CharField(max_length=128)
    last_name  = models.CharField(max_length=128)
    phone      = models.CharField(max_length=13)
    status     = models.CharField(max_length=1, choices=choices, default='z')

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