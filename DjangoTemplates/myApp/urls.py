from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页的
    url(r'^$', views.index),
    url(r'login/$', views.login, name='login'),
    # url(r'^login/$', views.index),
    url(r'^main/$', views.main),
]
