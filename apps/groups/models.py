from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.courses.models import Course
from apps.accounts.models import Student


class Group(models.Model):
    days_choices = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'friday'),
        ('Sat', 'Saturday'),
    )
    hours_choices = (
        (6, '06:00 AM'),
        (8, '08:00 AM'),
        (10, '10:00 AM'),
        (12, '12:00 AM'),
        (14, '02:00 PM'),
        (16, '04:00 PM'),
        (18, '06:00 PM'),
    )
    name       = models.CharField(max_length=64, unique=True)
    course     = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='groups')
    student    = models.ManyToManyField(Student, related_name='groups')

    days       = models.CharField(max_length=3, choices=days_choices)
    hours      = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(18)])

    started_at = models.DateField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
