from .models import Employee, Department
from choices import Supervisors, Departments

emp = Employee.objects.all()
print(emp)


