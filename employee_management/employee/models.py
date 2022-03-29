from django.db import models
from datetime import date
from .choices import Supervisors, Departments


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ''' foreigner key Employee '''



dept_list = []
emp = Department.objects.all()
for count,i in enumerate(emp,start=0):
    dept_list.append((count, i.name))

class Employee(models.Model):
    ''' '''

    usercode = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_leader = models.BooleanField(default=False)
    supervisor = models.PositiveSmallIntegerField(choices=Supervisors.SUPERVISORS, default=0)
    shift = models.PositiveSmallIntegerField(default=None, null=True)
    start_work = models.DateField(default=date.today)
    dept = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.usercode} - {self.first_name} {self.last_name}"



class Operations(models.Model):
    ''' foreigner key Employee '''
    name = models.CharField(max_length=255, unique=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

class Supervisors():
    BRAK, FIRST, SECOND = 0,1,2


    SUPERVISORS =  (
        (BRAK, 'brak'),
        (FIRST, 'Tomasz'),
        (SECOND, 'Iwona')
    )