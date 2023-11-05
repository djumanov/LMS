from django.db import models
from django.core.validators import MinValueValidator
from apps.accounts.models import Teacher, Student
from apps.groups.models import Group


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    group   = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.full_name
    

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    amount  = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(limit_value=0.00)])
    group   = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.full_name
    