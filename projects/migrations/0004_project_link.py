# Generated by Django 4.0.2 on 2022-03-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default=None, max_length=140),
        ),
    ]
