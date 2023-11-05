from django.db import models
from django.core.validators import MinValueValidator
from apps.courses.models import Assignment, Task
from apps.accounts.models import Student
    

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    assignment = models.ForeignKey(Assignment, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.student.full_name} - {self.assignment.name}"
    

class Submission(models.Model):
    attempts   = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
    is_correct = models.BooleanField()
    task       = models.ForeignKey(Task, on_delete=models.CASCADE)
    result     = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='submissions')

    def __str__(self):
        return self.task.name
