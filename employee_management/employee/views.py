from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from .models import Employee, Department, Operations
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NewUserForm, AddEmployeeForm



def glowna(request):
    employee = Employee.objects.all()
    ctx = {'employee': employee}
    return render(request,'main_side.html', ctx)

def register_request(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return render(request, "main_side.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):

    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')

# ----------------  CRUD Employee------------------------------------

class AddEmployee(LoginRequiredMixin, View):
    template = 'add_employee.html'
    success_url = reverse_lazy('employee:start')

    def get(self, request):
        form = AddEmployeeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = AddEmployeeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class EmployeeView(LoginRequiredMixin, View):
    template = 'employee_list.html'

    def get(self, request):
        employee = Employee.objects.all()
        print(employee)
        ctx = {'employee': employee}
        return render(request, self.template, ctx)

class EmployeeUpdate(LoginRequiredMixin, View):
    model = Employee
    success_url = reverse_lazy('employee:start')
    template = 'add_employee.html'

    def get(self, request, pk):
        employee = get_object_or_404(self.model, pk=pk)
        form = AddEmployeeForm(instance=employee)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        employee = get_object_or_404(self.model, pk=pk)
        form = AddEmployeeForm(request.POST, instance=employee)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class EmployeeDelete(LoginRequiredMixin, View):
    model = Employee
    success_url = reverse_lazy('employee:start')
    template = 'employee_confirm_delete.html'

    def get(self, request, pk):
        employee = get_object_or_404(self.model, pk=pk)
        form = AddEmployeeForm(instance=employee)
        ctx = {'employee': employee}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        employee = get_object_or_404(self.model, pk=pk)
        employee.delete()
        return redirect(self.success_url)

# ---------- CRUD Department

class DeptView(LoginRequiredMixin, View):
    template = 'department_list.html'

    def get(self, request):
        departments = Department.objects.all()
        ctx = {'departments': departments}
        return render(request, self.template, ctx)

class DeptCreate(LoginRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('employee:start')


class DeptUpdate(LoginRequiredMixin, UpdateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('employee:start')


class DeptDelete(LoginRequiredMixin, DeleteView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('employee:start')
    template = 'department_confirm_delete.html'


    def get(self, request, pk):
        department = get_object_or_404(self.model, pk=pk)
        form = AddEmployeeForm(instance=department)
        ctx = {'department': department}
        return render(request, self.template, ctx)