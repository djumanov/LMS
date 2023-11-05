from django.contrib import admin
from . import models


for_register = (
    models.Teacher,
    models.Student,
    models.Parent,
)

admin.site.register(for_register)