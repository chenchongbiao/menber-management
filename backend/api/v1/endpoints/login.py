from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request
from models import Admin
from core import verify_password, create_access_token, deps
from scheams import (
    UserIn_Pydantic,
    Response400,
    ResponseToken,
    Response200,
    User_Pydantic,
)

login = APIRouter(tags=["认证相关"])


@login.post("/login", summary="登录")
async def admin_login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    if admin := await Admin.get(username=form_data.username):
        if verify_password(form_data.password, admin.password):
            token = create_access_token({"sub": admin.username})
            # 使用redis时放开注释
            # await request.app.state.redis.set(user.username, token, 180)
            return ResponseToken(data={"token": f"bearer {token}"}, access_token=token)
    return Response400(msg="请求失败.")


@login.put("/logout", summary="注销")
async def admin_logout(request: Request, admin: Admin = Depends(deps.get_current_user)):
    request.app.state.redis.delete(admin.username)
    return Response200()


