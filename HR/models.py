from django.db import models
from django.contrib.auth.models import User
from company.models import Company


class Job(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=128)
    job = models.ManyToManyField(Job)
    user = models.OneToOneField(User,related_name="profile")
    company = models.ForeignKey(Company)
    
    def __unicode__(self):
        return self.name
    
    def get_jobs(self):
        return "\n".join([p.title for p in self.job.all()])