from django.db import models
from django.template.defaultfilters import slugify


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=999)
    phone = models.CharField(max_length=20)
    url = models.URLField(blank=True)
    slug = models.SlugField(unique=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name
