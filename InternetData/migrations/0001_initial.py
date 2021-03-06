# Generated by Django 2.0.5 on 2018-06-14 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(help_text='Enter comma(,) separated keywords')),
                ('type', models.CharField(choices=[('api', 'API'), ('scraper', 'Scraper'), ('crawler', 'Crawler'), ('other', 'Others')], default='api', max_length=15)),
                ('xpaths', models.TextField(blank=True)),
                ('urls', models.TextField(blank=True)),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Data Job List',
            },
        ),
        migrations.CreateModel(
            name='DataPipelines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Data Pipeline',
            },
        ),
        migrations.CreateModel(
            name='DataStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('unique_identity', models.CharField(max_length=30, unique=True)),
                ('type', models.CharField(choices=[('sink', 'SINK'), ('source', 'SOURCE')], default='sink', max_length=10)),
                ('host', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('username', models.CharField(blank=True, max_length=10)),
                ('password', models.SlugField(blank=True)),
                ('json_info', models.TextField(blank=True, default='{"DATABASE":"dbName", "COLLECTION":"collection"}')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Data Storage',
            },
        ),
        migrations.CreateModel(
            name='LoginMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('website', models.CharField(max_length=30)),
                ('token_key', models.CharField(help_text='Enter the token or Username here', max_length=100)),
                ('token_secret', models.CharField(blank=True, help_text='Enter the Token Secret or Password here', max_length=100)),
                ('consumer_key', models.CharField(blank=True, max_length=100)),
                ('consumer_secret', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Authentication Detail',
            },
        ),
        migrations.CreateModel(
            name='PipelineRunner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(default='test', max_length=20)),
                ('token', models.CharField(max_length=50)),
                ('username', models.CharField(default='admin', max_length=20)),
                ('password', models.CharField(default='nimda007#', max_length=50)),
                ('api_url', models.URLField(default='http://localhost:8080')),
                ('description', models.TextField(blank=True, help_text='This is a api based trigger for the code.\n                                                        Enter the REST API and Details. This is configured for Jenkins Job\n                                                        by default.\n                                                        ')),
            ],
            options={
                'verbose_name': 'Pipeline Job',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True)),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('project_jobs', models.ManyToManyField(to='InternetData.DataJob')),
            ],
            options={
                'verbose_name': 'Project',
            },
        ),
        migrations.CreateModel(
            name='ProjectPiplines',
            fields=[
                ('datapipelines_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='InternetData.DataPipelines')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True)),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Project Pipeline',
            },
            bases=('InternetData.datapipelines',),
        ),
        migrations.CreateModel(
            name='ScraperRunner',
            fields=[
                ('pipelinerunner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='InternetData.PipelineRunner')),
            ],
            options={
                'verbose_name': 'Data Scraper',
            },
            bases=('InternetData.pipelinerunner',),
        ),
        migrations.AlterUniqueTogether(
            name='datastore',
            unique_together={('name', 'host', 'json_info', 'type')},
        ),
        migrations.AddField(
            model_name='datapipelines',
            name='output',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='outputdata', to='InternetData.DataStore'),
        ),
        migrations.AddField(
            model_name='datapipelines',
            name='pipeline_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pipelines', to='InternetData.PipelineRunner'),
        ),
        migrations.AddField(
            model_name='datajob',
            name='data_pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datastore', to='InternetData.DataStore'),
        ),
        migrations.AddField(
            model_name='datajob',
            name='loginmeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keys', to='InternetData.LoginMeta'),
        ),
        migrations.AddField(
            model_name='datajob',
            name='pipelines',
            field=models.ManyToManyField(help_text='Multiple Pipelines Executed in Alphabetical Order', to='InternetData.DataPipelines'),
        ),
        migrations.AddField(
            model_name='projectpiplines',
            name='input',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputdata', to='InternetData.DataStore'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_pipeline',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_pipeline', to='InternetData.ProjectPiplines'),
        ),
        migrations.AddField(
            model_name='datajob',
            name='scraper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coderunner', to='InternetData.ScraperRunner'),
        ),
    ]
