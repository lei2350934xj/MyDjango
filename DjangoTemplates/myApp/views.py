from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . models import Students

def index(request):
    studentList = Students.objects.all()
    students = {}
    students['students'] = studentList
    students['str'] = 'i am chinese'
    students['list'] = ['good', 'nice', 'cool']
    students['origin'] = '<h1>origin 原样输出</h1>'
    return render(request, 'myApp/index.html', students)
    # return HttpResponse(student)
    # return HttpResponse('skr')

def login(request):
    return HttpResponse('login page ok!')

def main(request):
    return render(request,'myApp/main.html')


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
