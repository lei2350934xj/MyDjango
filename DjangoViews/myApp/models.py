from django.db import models

# Create your models here.

class Grades(models.Model):
    # 继承自 models.Model
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname
    class Meta:
        db_table = 'grades' # 这样数据库中的表名就是grades了 不然是myApp_grades


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(sgender=1)
    def createStudents(self, name, age, gender, contend, grade, ltime, ctime, isD=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = ltime
        stu.createTime = ctime
        return stu
        # print(type(stu))

class Students(models.Model):
    # 自定义模型管理器
    # stuObj = models.Manager()   # 于是模型管理器就是stuObj 不是 objects
    # stuObj = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)    # 关联外键
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname
    class Meta:
        db_table = 'students'
        ordering = ['id']   # 升序
        ordering = ['-id']  # 降序

    # 定义一个类方法创建对象
    # 1
    # def createStudents(Students, name, age, gender, contend, ltime, ctime):
    #     grade = Students(sname=name, sage=age, sgender=gender,
    #                 scontend=contend, lastTime=ltime, createTime=ctime)
    # 2
    @classmethod
    def createStudents(cls, name, age, gender, contend, grade, ltime, ctime, isD=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend,
                  sgrade=grade, lastTime=ltime, createTime=ctime, isDelete=isD)
        return stu