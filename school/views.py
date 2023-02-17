from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.db.models import Q
from .forms import StudentForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url='login')
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataq = Q(Q(fullname__icontains=q) | Q(email__icontains=q))
        students = Student.objects.filter(dataq)
    else:
        students = Student.objects.all()

    context = {'students': students}

    return render(request, 'school/home.html', context)


@login_required(login_url='login')
def teachers(request):

    allteachers = Teacher.objects.all()


    context = {'teachers': allteachers}

    return render(request, 'school/teachers.html', context)


@login_required(login_url='login')
def schoolname(request):

    schools = School.objects.all()

    context = {'schools': schools}

    return render(request, 'school/schools.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.cleaned_data.get('username')

            return redirect('login')

    context = {'registration_form': form}

    return render(request, 'school/registration.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'school/login.html', context)


def loginout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def create(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'school/studentform.html', context)


@login_required(login_url='login')
def update(request, pk):
    student = Student.objects.get(id=pk)

    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'school/studentform.html', context)


@login_required(login_url='login')
def delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('/')

    context = {'item': student}

    return render(request, 'school/delete_student.html', context)

