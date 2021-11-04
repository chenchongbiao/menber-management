from tortoise import models, fields


class Menu(models.Model):
    # id = fields.IntField(pk=True)
    icon = fields.CharField(max_length=100, null=True, description="图标")
    title = fields.CharField(max_length=30, null=True, description="标题")
    path = fields.CharField(max_length=30, null=True, description="路径")
    redirect = fields.CharField(max_length=30, null=True, description="重定向路径")
    component = fields.CharField(max_length=100, null=True, description="组件")
    status = fields.BooleanField(max_length=100, null=True, description="组件状态")
    name = fields.CharField(max_length=20, null=True, description="名字")
    orderNo = fields.IntField(null=True, description="排序编号")
    parent = fields.IntField(null=True, description="子路由",default=None)
    create_at = fields.DatetimeField(description="创建时间")
    update_at = fields.DatetimeField(description="更新时间")
    delete_at = fields.DatetimeField(description="删除时间")
