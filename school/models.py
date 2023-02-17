from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    gender = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )

    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    date_birth = models.DateField(max_length=50)
    student_course = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=100, choices=gender)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.fullname


class Teacher(models.Model):
    fullname = models.CharField(max_length=200)
    teacher_course = models.CharField(max_length=10, default='')
    lesson = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.lesson


class Course(models.Model):
    name_course = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name_course


class School(models.Model):
    name = models.CharField(max_length=150)
    courses = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name




# Create your models here.
