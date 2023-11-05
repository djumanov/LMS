from django.contrib import admin
from . import models


for_register = (
    models.Group,
)

admin.site.register(for_register)