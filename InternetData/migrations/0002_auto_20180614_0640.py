# Generated by Django 2.0.5 on 2018-06-14 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InternetData', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_jobs',
            new_name='data_jobs',
        ),
    ]
