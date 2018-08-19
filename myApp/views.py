from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('创建一个views')

def detail(request, num):
    return HttpResponse('viwes的详细信息%s'%num)

from . models import Grades
def grades(request):
    # 去模型里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板 模板再渲染页面 最后将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades.html', {'grades':gradesList})

from . models import Students
def students(request):
    # 去模型里取数据
    studentsList = Students.objects.all()
    # 将数据传递给模板 模板再渲染页面 最后将渲染好的页面返回给浏览器
    return render(request, 'myApp/students.html', {'students':studentsList})

def studentFrom(request, num):
    grade = Grades.objects.get(pk=num) # 当前的班级
    studentsList = grade.students_set.all() # 当前班级对应的所有学生
    return render(request, 'myApp/students.html', {'students':studentsList})

