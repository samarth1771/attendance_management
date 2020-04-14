from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime
import xlwt


# Create your views here.

def logins(request):
    # print("Inside login view")

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("gets post data")

        # This method returns userID if successfully validate
        user = authenticate(request, username=username, password=password)

        if user:  # if user is logged in successfully, redirect to student page
            login(request, user)
            print("Login done")
            return redirect('index')
        else:  # otherwise say Login failed
            return HttpResponse("Login Failed")
    print("End of login view")
    return render(request, 'login.html', {})


def log_out(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    return render(request, 'index.html', {})


@login_required
def insert(request):
    return render(request, 'insert.html', {})


@login_required
def edit(request):
    return render(request, 'edit.html', {})


@login_required
def view(request):
    return render(request, 'view.html', {})


@login_required
def view_attendance(request):
    return render(request, 'view_attendance.html', {})


@login_required
def insert_student(request):
    updated = False
    if updated == True:
        return render(request, 'insert_student.html', {'updated': updated})
        updated = False

    if request.method == 'POST':
        # print("This is er no", request.POST.get('er_no'))
        name = request.POST.get('name')
        er_no = int(request.POST.get('er_no'))
        rfid_no = int(request.POST.get('rfid_no'))
        dept = request.POST.get('dept')
        gender = request.POST.get('gender')
        semester = int(request.POST.get('sem'))
        st = Student(name=name, er_no=er_no, gender=gender, dept=dept, rfid_no=rfid_no, semester=semester)
        st.save()
        updated = True

        return render(request, 'insert_student.html', {'updated': updated})
    return render(request, 'insert_student.html', {})


@login_required
def insert_teacher(request):
    updated = False
    subs = Subject.objects.all()
    if updated == True:
        return render(request, 'insert_teacher.html', {'updated': updated, 'subs': subs})
        updated = False

    if request.method == 'POST':
        # print("This is er no", request.POST.get('tid'))
        name = request.POST.get('name')
        tid = int(request.POST.get('tid'))
        dept = request.POST.get('dept')
        subjects = request.POST.getlist('subjects')
        # print(subjects)
        t = Teacher(name=name, teacher_id=tid, dept=dept)
        t.save()
        for sub in subjects:
            t.subject_ids.add(sub)

        updated = True

        return render(request, 'insert_teacher.html', {'updated': updated, 'subs': subs})
    return render(request, 'insert_teacher.html', {'subs': subs})


@login_required
def insert_subject(request):
    updated = False
    if updated == True:
        return render(request, 'insert_subject.html', {'updated': updated})

    if request.method == 'POST':
        name = request.POST.get('name')
        sub_code = int(request.POST.get('sub_code'))
        semester = int(request.POST.get('sem'))
        s = Subject(name=name, sub_code=sub_code, semester=semester)
        s.save()
        updated = True

        return render(request, 'insert_subject.html', {'updated': updated})
    return render(request, 'insert_subject.html', {})


@login_required
def filter_student(request):
    filtered = False
    if filtered == True:
        return render(request, 'filter_student.html', {'filtered': filtered})

    std = Student.objects.all()
    std_dept = set()
    for s in std:
        std_dept.add(s.dept)
    print(std_dept)
    filtered = False

    return render(request, 'filter_student.html', {'std_dept': std_dept, 'filtered': filtered})


@login_required
def view_student(request):
    if request.method == "POST":
        dept = request.POST.get("dept")
        semester = request.POST.get("sem")

    filtered_std = Student.objects.filter(dept=dept, semester=semester)

    return render(request, 'view_student.html', {'filtered_std': filtered_std})


@login_required
def view_teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'view_teacher.html', {'teachers': teachers})


@login_required
def view_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'view_subject.html', {'subjects': subjects})


@login_required
def edit_student(request, id):
    if request.method == 'POST':
        # print("This is er no", request.POST.get('er_no'))
        # st = Student.objects.get(pk=int(request.POST.get('er_no')))

        name = request.POST.get('name')
        er_no = int(request.POST.get('er_no'))
        rfid_no = int(request.POST.get('rfid_no'))
        # print("This is the RFID", st.rfid_no)
        dept = request.POST.get('dept')
        gender = request.POST.get('gender')
        semester = int(request.POST.get('sem'))
        st = Student(name=name, er_no=er_no, gender=gender, dept=dept, rfid_no=rfid_no, semester=semester)
        st.save()
        updated = True
        return render(request, 'edit_student.html', {'std': st, 'updated': updated})

    st = Student.objects.get(pk=int(id))
    # print(st)
    std = Student.objects.all()
    std_dept = set()
    for s in std:
        std_dept.add(s.dept)
    # print(std_dept)

    return render(request, 'edit_student.html', {'std': st, 'std_dept': std_dept})


@login_required
def edit_teacher(request, id):
    if request.method == 'POST':
        # print("This is er no", request.POST.get('tid'))
        name = request.POST.get('name')
        tid = int(request.POST.get('tid'))
        dept = request.POST.get('dept')
        t = Teacher(name=name, teacher_id=tid, dept=dept)
        t.save()
        updated = True
        return render(request, 'edit_teacher.html', {'updated': updated})

    t = Teacher.objects.get(pk=int(id))
    subs = Subject.objects.all()
    std = Student.objects.all()
    std_dept = set()
    for s in std:
        std_dept.add(s.dept)

    return render(request, 'edit_teacher.html', {'teacher': t, 'subs': subs, 'std_dept': std_dept})


@login_required
def edit_subject(request, id):
    if request.method == 'POST':
        # print("This is er no", request.POST.get('tid'))
        name = request.POST.get('name')
        sub_code = int(request.POST.get('sub_code'))
        semester = int(request.POST.get('sem'))
        s = Subject(name=name, sub_code=sub_code, semester=semester)
        s.save()
        updated = True
        return render(request, 'edit_subject.html', {'updated': updated})

    subject = Subject.objects.get(pk=int(id))
    # subs = Subject.objects.all()
    # std = Student.objects.all()
    # std_dept = set()
    # for s in std:
    #     std_dept.add(s.dept)

    return render(request, 'edit_subject.html', {'subject': subject})


@login_required
def filter_attendance(request):
    std = Student.objects.all()
    subs = Subject.objects.all()
    teachers = Teacher.objects.all()
    std_dept = set()
    for s in std:
        std_dept.add(s.dept)
    # print(std_dept)

    if request.method == 'POST':
        subject = request.POST.get('subject')
        teacher = request.POST.get('teacher')
        dept = request.POST.get("dept")
        semester = request.POST.get("sem")

        filtered_std = Student.objects.filter(dept=dept, semester=semester)

        return render(request, 'attendance_filtered.html', {'filtered_std': filtered_std,
                                                            'subject': subject,
                                                            'teacher': teacher,
                                                            'dept': dept})

    return render(request, 'filter_attendance.html', {'std_dept': std_dept,
                                                      'subs': subs,
                                                      'teachers': teachers})


@login_required
def fill_attendance(request):
    if request.method == 'POST':
        students = request.POST.getlist('attendance')
        # print(students)
        teacher = Teacher.objects.get(name=request.POST.get('teacher'))
        subject = Subject.objects.get(name=request.POST.get('subject'))
        dept = request.POST.get('dept')
        # print(teacher,subject)
        for s in students:
            st = Student.objects.get(pk=s)
            date = datetime.date.today()
            time = datetime.datetime.now().time()
            At = Attendance(Student=st, attendance_time=time, attendance_date=date, Teacher=teacher, Subject=subject,
                            dept=dept)
            At.save()
            # print("Object created")
        return render(request, 'attendance_filtered.html', {'filled': True})

    return render(request, 'attendance_filtered.html', {'filled': False})


@login_required
def view_attendance(request):
    if request.method == 'POST' and 'show' in request.POST:
        subject = Subject.objects.get(name=request.POST.get('subject'))
        teacher = Teacher.objects.get(name=request.POST.get('teacher'))
        dept = request.POST.get("dept")
        # semester = request.POST.get("sem")
        d = request.POST.get("date")
        # print(d)
        date = datetime.datetime.strptime(d, "%Y-%m-%d").date()
        # print(date)
        Ats = Attendance.objects.filter(Subject=subject, Teacher=teacher, dept=dept, attendance_date=date)
        # for At in Ats:
        #     print(At.attendance_date)
        #     print(At.Subject)
        #     print(At.Teacher)
        #     print(At.Student)

        return render(request, 'show_attendance.html', {'subject': subject,
                                                        'teacher': teacher,
                                                        'dept': dept,
                                                        'date': date,
                                                        'Ats': Ats})

    elif request.method == 'POST' and 'download' in request.POST:

        subject = Subject.objects.get(name=request.POST.get('subject'))
        teacher = Teacher.objects.get(name=request.POST.get('teacher'))
        dept = request.POST.get("dept")
        # semester = request.POST.get("sem")
        d = request.POST.get("date")
        # print(d)
        date = datetime.datetime.strptime(d, "%Y-%m-%d").date()
        # print(date)
        Ats = Attendance.objects.filter(Subject=subject, Teacher=teacher, dept=dept, attendance_date=date)

        # content-type of response
        response = HttpResponse(content_type='application/ms-excel')
        file_name = str(subject) + ' ' + str(date) + '.xls'
        # decide file name
        # response['Content-Disposition'] = file_name + '.xls'
        # response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # column header names, you can use your own headers here
        columns = ['Teacher', 'ER No', 'Name', 'Subject', 'Department', 'Date', 'Time']

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # get your data, from database or from a text file...
        data = Ats  # dummy method to fetch data.
        for my_row in data:
            row_num = row_num + 1
            ws.write(row_num, 0, str(my_row.Teacher), font_style)
            ws.write(row_num, 1, str(my_row.Student), font_style)
            ws.write(row_num, 2, str(my_row.Student.name), font_style)
            ws.write(row_num, 3, str(my_row.Subject), font_style)
            ws.write(row_num, 4, str(my_row.dept), font_style)
            ws.write(row_num, 5, str(my_row.attendance_date), font_style)
            ws.write(row_num, 6, str(my_row.attendance_time), font_style)

        wb.save(response)
        return response

    std = Student.objects.all()
    subs = Subject.objects.all()
    teachers = Teacher.objects.all()
    std_dept = set()
    for s in std:
        std_dept.add(s.dept)
    print(std_dept)
    return render(request, 'view_attendance.html', {'std_dept': std_dept,
                                                    'subs': subs,
                                                    'teachers': teachers})
