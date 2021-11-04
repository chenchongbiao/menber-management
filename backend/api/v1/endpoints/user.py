from typing import List, Union
from fastapi import APIRouter, Depends
from core import deps
from models import User
from scheams import User_Pydantic, UserIn_Pydantic, Response200, Response400

user = APIRouter(tags=["会员信息相关"], dependencies=[Depends(deps.get_current_user)])
# user = APIRouter(tags=["会员信息相关"])


@user.get("/user", summary="会员列表", response_model=Union[Response200, Response400])
async def user_list(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    # elect * from user limit offset ,limit
    # select * from user  limit 0,10
    # return await User_Pydantic.from_queryset(User.all().offset(skip).limit(limit))
    result = {
        "total": await User.all().count(),
        "items": await User_Pydantic.from_queryset(User.all().offset(skip).limit(limit).order_by('-id'))
    }
    return Response200(
        result=result
    )

@user.post("/user", summary="新增会员信息")
async def user_add(user_form: UserIn_Pydantic):
    return Response200(
        result=await User_Pydantic.from_tortoise_orm(await User.create(**user_form.dict()))
    )


@user.put("/user/{pk}", summary="修改会员信息")
async def user_update(pk: int, user_form: UserIn_Pydantic):
    """
    修改会员信息
    """
    if await User.filter(pk=pk).update(**user_form.dict()):
        return Response200(result=await UserIn_Pydantic.from_tortoise_orm(user_form))
    return Response400(msg="更新失败")





@user.delete("/user/{pk}", summary="删除会员信息")
async def user_delete(pk: int):
    if await User.filter(pk=pk).delete():
        return Response200(msg="删除成功")
    return Response400(msg="删除失败")
