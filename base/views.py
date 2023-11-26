from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import Student

def HomePage(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        location = request.POST['location']
        
        newStudent = Student(first_name = firstName, last_name = lastName, phone_number = phoneNumber, email = email, location = location)
        newStudent.save()
    return render(request, 'account/signup.html', {})

def SuccessPage(request):
    return render(request, 'account/success.html')

