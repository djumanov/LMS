# Generated by Django 4.2.7 on 2023-11-05 13:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('is_correct', models.BooleanField()),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='results.result')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.task')),
            ],
        ),
    ]