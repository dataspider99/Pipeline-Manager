# Generated by Django 2.0.5 on 2018-06-19 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taxonomy', '0004_auto_20180619_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxonomy',
            name='keyword',
        ),
        migrations.AddField(
            model_name='keyword',
            name='taxonomy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='Taxonomy.Taxonomy'),
            preserve_default=False,
        ),
    ]
