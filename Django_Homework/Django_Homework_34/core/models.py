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
