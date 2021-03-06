# Generated by Django 2.0.5 on 2018-06-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InternetData', '0004_auto_20180614_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastore',
            name='json_info',
            field=models.TextField(blank=True, default='{}', help_text='\n    \n    Provide the other details in form of json string. For example:\n    Mongodb: {"DATABASE":"your database","COLLECTION":"your collection"}\n    Kafka: {"TOPIC":"your topic","GROUPID":"Group id"}\n    Elasticsearch: {"INDEX":"your index","TYPE":"document type"}\n    \n    '),
        ),
    ]
