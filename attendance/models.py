from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

GENDER = [('m', 'Male'), ('f', 'Female')]


class Student(models.Model):
    name = models.CharField(max_length=30)
    er_no = models.IntegerField(primary_key=True)
    rfid_no = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField()
    dept = models.CharField(max_length=10)
    gender = models.CharField(max_length=2, choices=GENDER, default='m')

    # image = models.ImageField(null=True, blank=True, upload_to="pics/")

    def __str__(self):
        return str(self.er_no)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    sub_code = models.IntegerField(primary_key=True)
    semester = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    teacher_id = models.IntegerField(primary_key=True)
    subject_ids = models.ManyToManyField(Subject)
    dept = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    Teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    dept = models.CharField(max_length=10)
    attendance_time = models.CharField(max_length=16)
    attendance_date = models.CharField(max_length=12)

    def __str__(self):
        return self.attendance_date
