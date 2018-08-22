from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('创建一个views')

def detail(request, num):
    return HttpResponse('viwes的详细信息%s'%num)

from . models import Grades
def grades(request):
    # 下面是超级经典的part：views.py主要负责去models里拿数据 再渲染到templates中 这样就做到了前后端分离 MVC
    # 去模型里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板 模板再渲染页面 最后将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades.html', {'grades':gradesList})

from . models import Students
from datetime import *

def students(request):
    # 去模型里取数据
    studentsList = Students.objects.all()
    # 将数据传递给模板 模板再渲染页面 最后将渲染好的页面返回给浏览器
    return render(request, 'myApp/students.html', {'students':studentsList})

def studentFrom(request, num):
    grade = Grades.objects.get(pk=num) # 当前的班级
    studentsList = grade.students_set.all() # 当前班级对应的所有学生
    return render(request, 'myApp/students.html', {'students':studentsList})


def addstudent(request):
    grade = Grades.objects.get(pk=1)
    # cls, name, age, gender, contend, grade
    stu = Students.createStudents('张学友',50,True,'我是学友大哥',
                grade, '2018-08-22', '2018-08-22')
    stu.save()
    return HttpResponse('添加学生成功')

def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    # cls, name, age, gender, contend, grade
    stu = Students.stuObj.createStudents('张学友',50,True,'我是学友大哥',
                grade, '2018-08-22', '2018-08-22')
    # stu.save()
    return HttpResponse('66666')

# 分页显示
def page(response, num):
    num = int(num)
    studentsList = Students.objects.all()[(num-1)*5:num*5]
    return render(response, 'myApp/students.html', {'students':studentsList})


# 数据库操作
# def testdb(request):
#     # 初始化
#     response = ""
#     response1 = ""
#
#     # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
#     list = Test.objects.all()
#
#     # filter相当于SQL中的WHERE，可设置条件过滤结果
#     response2 = Test.objects.filter(id=1)
#
#     # 获取单个对象
#     response3 = Test.objects.get(id=1)
#
#     # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
#     Test.objects.order_by('name')[0:2]
#
#     # 数据排序
#     Test.objects.order_by("id")
#
#     # 上面的方法可以连锁使用
#     Test.objects.filter(name="runoob").order_by("id")
#
#     # 输出所有数据
#     for var in list:
#         response1 += var.name + " "
#     response = response1
#     return HttpResponse("<p>" + response + "</p>")
