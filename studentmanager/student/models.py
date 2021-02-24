from django.db import models

# Create your models here.

class students(models.Model):

    GENDER_CHOICES = (
        (0, "male"),
        (1, "female")
    )
    name = models.CharField(max_length=10, db_index=True, verbose_name="姓名")
    age = models.IntegerField(default=18, verbose_name="年龄")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name="性别")
    # height = models.FloatField(default=None, verbose_name="身高")\
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="身高")
    birthday = models.DateField(default=None, verbose_name="出生日期")
    classes = models.ForeignKey('classes', to_field='id', default=1, on_delete=models.PROTECT)

    id_delete = models.BooleanField(default=False, verbose_name="删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "students"
        verbose_name = "学生信息"

    def __str__(self):
        return self.name


class subject(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="课程名")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "subject"
        verbose_name = "课程信息"

    def __str__(self):
        #定义每个数据对象的显示信息
        return self.name


class classes(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="班级名称")
    create_at = models.DateField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "classes"
        verbose_name = "班级信息"

    def __str__(self):
        return self.name


