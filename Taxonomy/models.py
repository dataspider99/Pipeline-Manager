from django.db import models

# Create your models here.
    
class Taxonomy(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=True)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Prjoect(models.Model):
    name = models.CharField(max_length=50)
    taxonomy = models.ManyToManyField(Taxonomy) 

    def __str__(self):
        return self.name
    
class Keyword(models.Model):
    
    taxonomy = models.ForeignKey(Taxonomy,related_name='keywords',on_delete=models.CASCADE)
    level1 = models.CharField(max_length=30,blank=True)
    level2 = models.CharField(max_length=30,blank=True)
    level3 = models.CharField(max_length=30,blank=True)
    level4 = models.CharField(max_length=30,blank=True)
    level5 = models.CharField(max_length=30,blank=True)
    keyword = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword