from django.contrib import admin

# Register your models here.

from .models import Grades, Students

class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

'''
    站点管理
'''
@admin.register(Grades) # 用装饰器来注册
class GradesAdmin(admin.ModelAdmin):
    # 创建一个班级，分配2个学生
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5 # 多少条记录分页

    # 添加页和修改页属性（两个页面）
    fields = ['gname','gdate','ggirlnum','gboynum']
    # fieldsets = []

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别' # 设置页面列的名称
    list_display = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', 'isDelete']
    list_per_page = 10

    actions_on_top = False # 执行动作的位置
    actions_on_bottom = True

# 注册
# admin.site.register(Grades,GradesAdmin)
# admin.site.register(Students,StudentsAdmin)

