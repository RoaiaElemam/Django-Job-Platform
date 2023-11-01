from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

JOB_TYPE = (
    ('full time','full time') ,#('for data base' , 'for user')
    ('part time','part time'),
    ('remote','remote'),
    ('freelance','freelance'),

)
# Create your models here.
class Job (models.Model):
    title=models.CharField(max_length=120)
    location= CountryField()
    created_at=models.DateTimeField(default=timezone.now)
    company=models.ForeignKey('Company',on_delete=models.CASCADE,related_name='job_company')
    salary_start=models.IntegerField(null=True,blank=True)
    salary_end=models.IntegerField(null=True,blank=True)
    description=models.TextField(max_length=1500)
    vacancy=models.IntegerField()
    job_type=models.CharField(choices=JOB_TYPE,max_length=10)
    experince=models.IntegerField()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True,related_name='job_category')
    
    def __str__(self):
      return self.title


class Category (models.Model):
    name=models.CharField(max_length=30)
    logo=models.CharField(max_length=30)

    def __str__(self):
      return self.name


class Company (models.Model):
    name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='company')
    subtitle=models.TextField(max_length=1000)
    website=models.URLField()
    email=models.EmailField()

    def __str__(self):
      return self.name