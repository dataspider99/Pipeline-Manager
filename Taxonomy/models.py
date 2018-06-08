from django.db import models

# Create your models here.
class Taxonomy(models.Model):
    name = models.CharField(max_length=30,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Keywords(models.Model):
    
    taxonomy = models.ForeignKey(Taxonomy,related_name='keywords',on_delete=models.CASCADE)
    level1 = models.CharField(max_length=30,blank=True)
    level2 = models.CharField(max_length=30,blank=True)
    level3 = models.CharField(max_length=30,blank=True)
    level4 = models.CharField(max_length=30,blank=True)
    level5 = models.CharField(max_length=30,blank=True)
    keyword = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword