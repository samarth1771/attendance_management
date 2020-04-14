"""attendance_revamped URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from attendance.views import *

urlpatterns = [
    path('', logins, name='login'),
    path('logout/', log_out, name='logout'),
    path('index/', index, name='index'),
    path('insert/', insert, name='insert'),
    path('edit/', edit, name='edit'),
    path('view_attendance/', view_attendance, name='view_attendance'),
    path('insert/student/', insert_student, name='insert_student'),
    path('insert/teacher/', insert_teacher, name='insert_teacher'),
    path('insert/subject/', insert_subject, name='insert_subject'),
    path('edit/filter/student', filter_student, name='filter_student'),
    path('filter/attendance', filter_attendance, name='filter_attendance'),
    path('view_student', view_student, name='view_student'),
    path('view_subject', view_subject, name='view_subject'),
    path('view_teacher', view_teacher, name='view_teacher'),
    path('edit/student/<int:id>', edit_student, name='edit_student'),
    path('edit/teacher/<int:id>', edit_teacher, name='edit_teacher'),
    path('edit/subject/<int:id>', edit_subject, name='edit_subject'),
    path('fill_attendance', fill_attendance, name='fill_attendance'),
    # path('show_attendance', show_attendance, name='show_attendance'),

]
