# Generated by Django 2.0.5 on 2018-06-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InternetData', '0003_auto_20180607_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acquiredata',
            name='available',
        ),
        migrations.AlterField(
            model_name='acquiredata',
            name='type',
            field=models.CharField(choices=[('a', 'API'), ('s', 'Scraper'), ('c', 'Crawler')], default='a', max_length=10),
        ),
    ]
