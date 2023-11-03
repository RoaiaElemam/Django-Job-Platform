import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random 
from job.models import Category,Company,Job

def create_category(n):
    fake = Faker()
    for x in range(n):
        Category.objects.create(
            name=fake.name()
        )
    print(f"{n}category was added sucessfully")

def create_company(n):
    faker = Faker()
    images=['job-list1.png','job-list2.png','job-list3.png','job-list4.png']
    for x in range(n):
        Company.objects.create(
            name=faker.company(),
            website=faker.url(),
            subtitle=faker.text(),
            email=faker.email(),
            logo = f"company/{images[random.randint(0,3)]}"

        )
    print(f"{n}company was added sucessfully")


def create_job(n):
   
   faker = Faker()
   job_type=['full time','part time','remote','freelance']

   for x in range(n):
       Job.objects.create(
           title=faker.name(),
           description=faker.sentence(),
           company=Company.objects.all().order_by('?')[0],
           vacancy=random.randint(1,5),
           salary_start=random.randint(2000,2500),
           salary_end=random.randint(2300,2800),
           experince=random.randint(1,10),
           category=Category.objects.all().order_by('?')[0],
           job_type=job_type[random.randint(0,3)]

        )
    #print(f"{n}job was added sucessfully")

    


create_category(5)
create_company(100)
create_job(1000)




