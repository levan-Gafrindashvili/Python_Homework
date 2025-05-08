from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# 36) myapp/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
