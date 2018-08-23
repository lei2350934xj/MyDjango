from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # 取session的值
    username = request.session.get('username','游客')
    print(username)

    return render(request, 'myApp/index.html', {'username':username})

def login(request):
    return render(request, 'myApp/login.html')

def showindex(request):
    print('showindex start')
    # 获取
    username = request.POST.get('username')
    # 存
    request.session['username'] = username
    request.set_expiry(10)  # 设置过期时间
    return redirect('/index')

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
from django.db.models import Max    # 引入聚合函数

def students(request):
    # 去模型里取数据
    studentsList = Students.objects.all()
    # 将数据传递给模板 模板再渲染页面 最后将渲染好的页面返回给浏览器
    return render(request, 'myApp/students.html', {'students':studentsList})

def studentFrom(request, num):
    grade = Grades.objects.get(pk=num) # 当前的班级
    studentsList = grade.students_set.all() # 当前班级对应的所有学生
    return render(request, 'myApp/students.html', {'students':studentsList})

# 在views.py中调用创建对象的方法 完成对象的创建 再调用save()实现写入数据库
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
def page(request, num):
    num = int(num)
    studentsList = Students.objects.all()[(num-1)*5:num*5]
    return render(request, 'myApp/students.html', {'students':studentsList})

def studentSearch(request):
    studentsList = Students.objects.filter(sname__contains='孙')
    return render(request, 'myApp/students.html', {'students':studentsList})

def findMax(request):
    studentsList = Students.objects.aggregate(Max('sage'))
    print(studentsList)
    return render(request, 'myApp/students.html', {'students':studentsList})

from django.db.models import F,Q
def JudgeF(request):
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
    print(g)
    return HttpResponse(g)

def JudgeQ(request):
    studentsList = Students.objects.filter(Q(pk__lt=2) | Q(sage=50))
    return render(request, 'myApp/students.html', {'students':studentsList})

def attribute(request):
    print(request.GET)
    print(request.path)
    return HttpResponse('skr skr skr')


def httpresponse(request):
    res = HttpResponse()
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res


def cookietest(request):
    res = HttpResponse()
    # 设置cookie
    cookie = res.set_cookie("lttt","adad ")
    # 获取cookie
    getCookie = request.COOKIES
    return HttpResponse(getCookie)

# 重定向
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
def redirect1(request):
    # 重定向到redirect2去
    return HttpResponseRedirect('/redirect2')
    # return redirect('redirect2')

def redirect2(request):
    return HttpResponse('我是重定向后的视图')



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
