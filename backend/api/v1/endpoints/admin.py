from typing import Union
from fastapi import APIRouter, Depends
from core import deps, get_password_hash
from models import Admin
from scheams import Admin_Pydantic, AdminIn_Pydantic, Response200, Response400

admin = APIRouter(tags=["管理员相关"], dependencies=[Depends(deps.get_current_user)])
# admin = APIRouter(tags=["管理员相关"])


@admin.get("/admin", summary="获取当前用户信息信息")
async def admin_info(user_obj: Admin = Depends(deps.get_current_user)):
    """
    - username: str 必传
    - password: str 必传
    """
    return Response200(result=await Admin_Pydantic.from_tortoise_orm(user_obj))


@admin.get("/system/getAccountList", summary="获取账户列表", response_model=Union[Response200, Response400])
async def admin_list(page: int = 1, pagesize: int = 10):
    skip = (page - 1) * pagesize
    # elect * from admin limit offset ,limit
    # select * from admin  limit 0,10
    result = {
        "total": await Admin.all().count(),
        "items": await Admin_Pydantic.from_queryset(Admin.all().offset(skip).limit(pagesize).order_by('-id'))
    }
    return Response200(
        result=result
    )

    # return await Admin_Pydantic.from_queryset(Admin.all().offset(skip).limit(pagesize))


@admin.get("/account_detail/{pk}", summary="获取指定用户信息信息")
async def admin_find(pk: int, user_obj: Admin = Depends(deps.get_current_user)):
    """
    - username: str 必传
    - password: str 必传
    """
    user = await Admin.filter(pk=pk).first()
    if user:
        return Response200(result=user)


@admin.post("/admin", summary="管理员新增")
async def admin_add(admin: AdminIn_Pydantic):
    return Response200(
        result=await Admin_Pydantic.from_tortoise_orm(await Admin.create(**admin.dict()))
    )


@admin.put("/admin", summary="修改当前用户信息")
async def admin_update(user_form: AdminIn_Pydantic, user_obj: Admin = Depends(deps.get_current_user)):
    """
    修改当前用户信息
    """
    # user_form.username = user_obj.username
    user_form.password = get_password_hash(user_obj.password)
    if await Admin.filter(username=user_obj.username).update(**user_form.dict()):
        return Response200(result=await Admin_Pydantic.from_tortoise_orm(user_form))
    return Response400(msg="更新失败")


@admin.delete("/admin/{pk}", summary="删除指定用户")
async def admin_delete(pk: int):
    if await Admin.filter(pk=pk).delete():
        return Response200(msg="删除成功")
    return Response400(msg="删除失败")
