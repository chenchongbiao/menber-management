from typing import Optional, Iterable
from tortoise import models, fields, BaseDBAsyncClient
from core import get_password_hash


class Admin(models.Model):
    username = fields.CharField(max_length=20, null=False, description="账号")
    password = fields.CharField(max_length=128, null=False, description="密码")
    nickname = fields.CharField(max_length=20, null=True, description="昵称", default="管理员")
    email = fields.CharField(max_length=30, null=True, description="邮箱")
    role = fields.CharField(max_length=20, null=True, description="角色")
    remark = fields.CharField(max_length=50, null=True, description="备注")
    create_at = fields.DatetimeField(description="创建时间")
    update_at = fields.DatetimeField(description="更新时间")
    delete_at = fields.DatetimeField(description="删除时间")

    async def save(
            self,
            using_db: Optional[BaseDBAsyncClient] = None,
            update_fields: Optional[Iterable[str]] = None,
            force_create: bool = False,
            force_update: bool = False,
    ) -> None:
        if force_create or "password" in update_fields:
            self.password = get_password_hash(self.password)

        await super(Admin, self).save(using_db, update_fields, force_create, force_update)
