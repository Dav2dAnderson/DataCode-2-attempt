# Generated by Django 5.2.4 on 2025-07-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
