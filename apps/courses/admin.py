from django.contrib import admin
from . import models


for_register = (
    models.Course,
    models.Module,
    models.Lesson,
    models.VideoType,
    models.Video,
    models.MaterialType,
    models.Material,
    models.AssignmentType,
    models.Assignment,
    models.Task,
    models.Quiz,
    models.QuestionType,
    models.Question,
    models.Option,
)

admin.site.register(for_register)
