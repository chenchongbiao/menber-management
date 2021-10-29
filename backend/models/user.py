from tortoise import models,fields

class User(models.Model):
    number = fields.IntField(max_length=5, null=True, description="会员号")
    name = fields.CharField(max_length=20, null=True, description="姓名")
    std_num = fields.IntField(max_length=12, null=True, description="学号")
    sex = fields.IntField(max_length=1, null=True, description="性别", default="1")
    college = fields.CharField(max_length=20, null=True, description="学院")
    class_and_grade = fields.CharField(max_length=1, null=True, description="班级", default="1")
    native_place = fields.CharField(max_length=20, null=True, description="籍贯")
    wechat = fields.CharField(max_length=50, null=True, description="微信号")
    phone = fields.CharField(max_length=11, null=True, description="电话")
    email = fields.CharField(max_length=20, null=True, description="邮箱")

