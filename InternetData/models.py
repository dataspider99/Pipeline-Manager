from django.db import models

class CodeRunner(models.Model):
    name = models.CharField(max_length=10)
    token = models.CharField(max_length = 50)
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 50)
    api_url = models.URLField()
    jobname = models.CharField( max_length= 20,default="testjob")
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    
class LoginMeta(models.Model):
    class Meta:
        unique_together = (('name','token_key'))
    name = models.CharField(max_length=30,default="Anonymus")
    website = models.CharField(max_length=30)
    token_key = models.CharField(max_length=100,help_text="Enter the token or Username here")
    token_secret = models.CharField(max_length=100, blank=True,help_text="Enter the Token Secret or Password here")
    consumer_key = models.CharField(max_length=100, blank=True)
    consumer_secret = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.website +":"+ self.token_key  

class DataStore(models.Model):
    name = models.CharField(max_length=10)
    host = models.CharField(max_length=50)
    port = models.IntegerField()
    username = models.CharField(max_length=10,blank=True)
    password = models.SlugField(blank=True)
    json_info = models.TextField(blank=True,default='{"db":"dbName", "collection":"collection"}')
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
        
class AcquireData(models.Model):
    api = 'a'
    scraper = 's'
    crawler = 'c'
    choices = ((api,"API"),(scraper,"Scraper"),(crawler,"Crawler"))
    
    loginmeta = models.ForeignKey(LoginMeta,on_delete=models.CASCADE,related_name="keys")
    keywords = models.TextField(help_text="Enter comma(,) separated keywords")
    datastore = models.ForeignKey(DataStore,on_delete=models.CASCADE,related_name="datastore")
    coderunner = models.ForeignKey(CodeRunner,on_delete=models.CASCADE,related_name="coderunner")
    type = models.CharField(max_length=10,choices=choices,default=api)
    xpaths = models.TextField(blank=True)
    urls = models.TextField(blank=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True) 
    isactive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.loginmeta.website+":"+self.keywords
    class Meta:
        verbose_name = 'API'
    
    

    
