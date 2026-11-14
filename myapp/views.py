from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact, Employee

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('home')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('home')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('home')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'User created successfully')
            return redirect('home')

    return render(request, 'home.html')
def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(full_name=full_name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')
def employee(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        department = request.POST.get('department')
        hire_date = request.POST.get('hire_date')

       
        new_employee = Employee(
            full_name=fullname,
            email=email,
            position=position,
            department=department,
            hire_date=hire_date
        )
        new_employee.save()
        messages.success(request, 'Employee added successfully!')
        return redirect('employee')

    return render(request, 'employee.html')