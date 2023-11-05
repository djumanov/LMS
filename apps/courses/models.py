from django.db import models
from django.core.validators import MinValueValidator


class Course(models.Model):
    title       = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(limit_value=0.00)])

    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Module(models.Model):
    number      = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
    title       = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)
    course      = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='modules')

    def __str__(self):
        return f"{self.number}. {self.title}"

    
class Lesson(models.Model):
    number      = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
    title       = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)
    module      = models.ForeignKey(Module, on_delete=models.DO_NOTHING, related_name='lessons')

    def __str__(self):
        return f"{self.number}. {self.title}"


class VideoType(models.Model):
    type = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.type
    

class Video(models.Model):
    title  = models.CharField(max_length=264)
    link   = models.URLField()
    type   = models.ForeignKey(VideoType, on_delete=models.DO_NOTHING)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class MaterialType(models.Model):
    type = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.type


class Material(models.Model):
    title  = models.CharField(max_length=264)
    link   = models.URLField()
    type   = models.ForeignKey(MaterialType, on_delete=models.DO_NOTHING)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    

class AssignmentType(models.Model):
    type = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.type


class Assignment(models.Model):
    name        = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    link        = models.URLField(blank=True, null=True)
    lesson      = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, related_name='assignments')

    def __str__(self):
        return self.name
    

class Task(models.Model):
    number     = models.IntegerField(validators=[MinValueValidator(limit_value=1)])
    name       = models.CharField(max_length=64)
    assignment = models.ForeignKey(Assignment, on_delete=models.DO_NOTHING, related_name='tasks')


class Quiz(models.Model):
    title      = models.CharField(max_length=264)
    assignment = models.ForeignKey(Assignment, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    
class QuestionType(models.Model):
    type = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.type


class Question(models.Model):
    question = models.CharField(max_length=512)
    type     = models.ForeignKey(QuestionType, on_delete=models.DO_NOTHING)
    quiz     = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.question


class Option(models.Model):
    option     = models.CharField(max_length=512)
    is_correct = models.BooleanField()
    question   = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.option

