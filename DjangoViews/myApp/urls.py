from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页的
    url(r'^$', views.index),
    url(r'^(\d+)/$', views.detail),

    # grades的
    url(r'^grades/$', views.grades),
    # students的
    url(r'^students/$', views.students),
    # 对应班级的
    url(r'^grades/(\d+)$', views.studentFrom),
    # 增加一个学生
    url(r'^addstudent/$', views.addstudent),
    # 分页显示
    url(r'^students/(\d+)/$', views.page),
    # 查询
    url(r'^studentSearch/$', views.studentSearch),
    # 查看年龄最大的
    url(r'^age/$', views.findMax),
    # 比较男女比例
    url(r'^JudgeF/$', views.JudgeF),
    url(r'^JudgeQ/$', views.JudgeQ),
    # 利用GET属性获取url请求内容
    url(r'^attribute/$', views.attribute),
    # 查看HttpResponse
    url(r'^httpresponse/$', views.httpresponse),
    # 设置cookie
    url(r'^cookietest/$', views.cookietest),
    # 重定向
    url(r'redirect1/$', views.redirect1),
    url(r'redirect2/$', views.redirect2),

    url(r'^index/$', views.index),
    # url(r'^index/login/$', views.login),
    url(r'^login/$', views.login),
    # url(r'^index/login/showIndex/$', views.showindex)
    url(r'^showIndex/$', views.showindex)

]
