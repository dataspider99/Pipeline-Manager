# Generated by Django 2.0.5 on 2018-06-19 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level1', models.CharField(blank=True, max_length=30)),
                ('level2', models.CharField(blank=True, max_length=30)),
                ('level3', models.CharField(blank=True, max_length=30)),
                ('level4', models.CharField(blank=True, max_length=30)),
                ('level5', models.CharField(blank=True, max_length=30)),
                ('keyword', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='keywords',
            name='taxonomy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='Taxonomy.Taxonomy'),
        ),
    ]