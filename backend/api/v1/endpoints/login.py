from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request
from models import Admin
from core import verify_password, create_access_token, deps
from scheams import (
    Response400,
    ResponseToken,
    Response200,
)

login = APIRouter(tags=["认证相关"])


@login.post("/login", summary="登录")
async def admin_login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    if admin := await Admin.get(username=form_data.username):
        if verify_password(form_data.password, admin.password):
            token = create_access_token({"sub": admin.username})
            # 使用redis时放开注释
            # await request.app.state.redis.set(user.username, token, 180)
            return ResponseToken(
                result={"token": f"bearer {token}", "roles": ["admin"], "username": form_data.username},
                access_token=token)
    return Response400(msg="请求失败.")

@login.get("/getUserInfo", summary="获取用户角色和用户名")
def admin_info(user_obj: Admin = Depends(deps.get_current_user)):
    """
    - username: str 必传
    - password: str 必传
    """
    data = {
        "roles": [user_obj.role],
        "username": user_obj.username
    }
    return Response200(result=data)

@login.get("/getPermCode", summary="code编码")
async def admin_perm_code():
    data = {
        '1': ['1000', '3000', '5000']
    }
    return Response200(result={"code": data})


@login.get("/logout", summary="注销")
async def admin_logout(request: Request, admin: Admin = Depends(deps.get_current_user)):
    # redis中删除该用户
    # request.app.state.redis.delete(admin.username)
    return Response200()
