import secrets
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE: Optional[str] = "会员信息管理接口"
    DESC: Optional[str] = """
    - 会员信息管理项目
    - 实现： FastAPI ....
    """

    # JWT
    # token相关
    ALGORITHM: str = "HS256"  # 加密算法
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3

    ORIGINS = [
        "http://localhost:3000"
        "http://127.0.0.1:3000"
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "*"
    ]


settings = Settings()
