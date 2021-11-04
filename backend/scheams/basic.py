from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    """业务状态码"""
    SUCCESS = 0
    FAIL = 1


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="业务状态码 0 是成功, 1 是失败")
    result: Any = Field(default=None, description="数据结果")
    msg: str = Field(default="请求成功", description="提示")


class Response200(ResponseBasic):
    pass

class ResponseToken(Response200):
    access_token: str
    token_type: str = Field(default="bearer")


class Response400(ResponseBasic):
    code: CodeEnum = CodeEnum.FAIL
    msg: str = "请求失败"
