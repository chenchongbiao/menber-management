from typing import Union
from fastapi import APIRouter, Depends
from core import deps
from models import Menu
from scheams import Response200, Response400, Menu_Pydantic, MenuIn_Pydantic

menu = APIRouter(tags=["菜单相关"], dependencies=[Depends(deps.get_current_user)])
# menu = APIRouter(tags=["菜单相关"])


@menu.get("/menu/list", summary="菜单列表", response_model=Union[Response200, Response400])
async def menu_list():
    # result = {
    #     "total": await Menu.all().count(),
    #     "items": await Menu_Pydantic.from_queryset(Menu.all())
    # }
    # exclude排除掉子路由为空路由
    result = []
    menu_list = await Menu_Pydantic.from_queryset(Menu.filter(parent=0).all())
    for menu in menu_list:
        childrens = await Menu_Pydantic.from_queryset(Menu.filter(parent=menu.id).all())
        children_list = []
        for children in childrens:
            children = dict(children)
            children["meta"] = {"title": children["name"]}
            children_list.append(children)
        menu = dict(menu)
        menu["children"] = children_list
        menu["meta"] =  {"title": menu["name"]}
        result.append(menu)
    return Response200(
        result=result
    )


@menu.post("/menu", summary="新增菜单信息")
async def user_add(user_form: MenuIn_Pydantic):
    return Response200(
        result=await Menu_Pydantic.from_tortoise_orm(await Menu.create(**user_form.dict()))
    )
