from django.contrib import admin
from .models import Attendance, Payment


admin.site.register(
    (Attendance, Payment)
)
