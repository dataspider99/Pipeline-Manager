# Generated by Django 2.0.5 on 2018-06-15 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InternetData', '0006_auto_20180615_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datajob',
            name='data_pool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datastore', to='InternetData.DataStore'),
        ),
    ]
