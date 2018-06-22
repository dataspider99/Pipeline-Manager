from django.db import models


class DataStore(models.Model):
    class Meta:
        verbose_name="Data Storage"
        unique_together = (('name','host','json_info','type'))
    sink = 'sink'
    source = 'source'
    choices = ((sink,"SINK"),(source,"SOURCE"))
    
    name = models.CharField(max_length=30)
    unique_identity = models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=10,choices=choices,default=sink)
    host = models.CharField(max_length=50)
    port = models.IntegerField()
    username = models.CharField(max_length=10,blank=True)
    password = models.SlugField(blank=True)
    json_info = models.TextField(blank=True,default='{}',help_text="""
    
    Provide the other details in form of json string. For example:
    Mongodb: {"DATABASE":"your database","COLLECTION":"your collection"}
    Kafka: {"TOPIC":"your topic","GROUPID":"Group id"}
    Elasticsearch: {"INDEX":"your index","TYPE":"document type"}
    
    """)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.unique_identity+":"+self.name +":"+self.type

    
class LoginMeta(models.Model):
    class Meta:
        verbose_name="Data Auth"
    name = models.CharField(max_length=30,unique=True)
    website = models.CharField(max_length=30)
    token_key = models.CharField(max_length=200,help_text="Enter the token or Username here")
    token_secret = models.CharField(max_length=200, blank=True,help_text="Enter the Token Secret or Password here")
    consumer_key = models.CharField(max_length=200, blank=True)
    consumer_secret = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name +":"+ self.token_key  

class PipelineRunner(models.Model):
    jobname = models.CharField( max_length= 30,default="test")
    login = models.ForeignKey(LoginMeta,on_delete=models.CASCADE,related_name="credentials")
    api_url = models.URLField(default="http://localhost:8080")
    description = models.TextField(blank=True,help_text="""This is a api based trigger for the code.
                                                        Enter the REST API and Details. This is configured for Jenkins Job
                                                        by default.
                                                        """)
    
    def __str__(self):
        return self.jobname
    class Meta:
        verbose_name = "Pipeline Job"

class ScraperRunner(PipelineRunner):
    class Meta:
        verbose_name = "Data Scraper"
    
    @property
    def get_id(self):
        if self.id:
            return self.id
        else:
            return "0"
        
class DataPipelines(models.Model):
    pipeline_job = models.ForeignKey(PipelineRunner, on_delete=models.CASCADE,related_name="pipelines")
    output = models.OneToOneField(DataStore,on_delete=models.CASCADE,related_name="outputdata")
    
    def __str__(self):
        return self.pipeline_job.jobname
    
    @property
    def get_name(self):
        return self.pipeline_job.jobname
    
    class Meta:
        verbose_name="Data Pipeline"
    
class DataJob(models.Model):
    class Meta:
        verbose_name="Data Job List"
    api = 'api'
    scraper = 'scraper'
    crawler = 'crawler'
    others = 'other'
    choices = ((api,"API"),(scraper,"Scraper"),(crawler,"Crawler"),(others,'Others'))
    desc = models.CharField(max_length=50, default="Please insert 50 Char Description")
    loginmeta = models.ForeignKey(LoginMeta,on_delete=models.CASCADE,related_name="keys",null=True,blank=True)
    keywords = models.TextField(help_text="Enter comma(,) separated keywords")
    scraper = models.ForeignKey(ScraperRunner,on_delete=models.CASCADE,related_name="coderunner",null=True,blank=True)
    type = models.CharField(max_length=15,choices=choices,default=api)
    xpaths = models.TextField(blank=True)
    urls = models.TextField(blank=True)
    data_pool = models.ForeignKey(DataStore,on_delete=models.CASCADE,related_name="datastore",null=True,blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    pipelines = models.ManyToManyField(DataPipelines,help_text="Multiple Pipelines Executed in Alphabetical Order") 
    isactive = models.BooleanField(default=False)
    
    @property
    def get_loginmeta(self):
        return self.loginmeta.website
    
    @property
    def get_datastore(self):
        return self.datapool.name
    
    @property
    def get_coderunner(self):
        return self.scraper.jobname
        
    def save(self, *args, **kwargs):
        try:
            self.datapool
        except:
            self.datapool = DataStore.objects.first()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.desc+" Type:"+self.type+":"+self.keywords
    
class ProjectPiplines(DataPipelines):
    input = models.ForeignKey(DataStore, on_delete=models.CASCADE,related_name="inputdata")
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name+":"+self.description
    
    class Meta:
        verbose_name="Project Pipeline"
    
class Project(models.Model):
    project_name = models.CharField(max_length=30, unique=True)
    data_jobs = models.ManyToManyField(DataJob)
    project_pipeline = models.OneToOneField(ProjectPiplines,on_delete=models.CASCADE,related_name="project_pipeline")
    description = models.TextField(blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
     
    class Meta:
        verbose_name="Project"
    
    def __str__(self):
        return self.project_name
    
    @property
    def get_name(self):
        return self.project_name
