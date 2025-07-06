import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CURDproject.settings')
import django
django.setup()
from testapp.models import Employee
from random import *
from faker import Faker
faker=Faker()

def populate(n):
    for i in range(n):
        feno=randint(1,50)
        fename=faker.name()
        fsal=randint(10000,25000)
        faddress=faker.city()
        emp_record=Employee.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fsal,
            eaddress=faddress
        )
n=int(input("Enter U have Generate:"))
populate(n)
print(f"{n} inserted record successfully................")