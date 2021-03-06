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
    url(r'^grades/(\d+)$', views.studentFrom)
]