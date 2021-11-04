import sys
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from .v1 import v1
from fastapi import FastAPI
import logging
from core import settings
# from core.config import settings
app = FastAPI(
    title=settings.TITLE,
    description=settings.DESC,
    version='1.0.0',
    docs_url='/docs',  # docs文档地址
    redoc_url='/redocs'# redocs文档地址
)

app.include_router(v1, prefix="/api")

# redis进行用户数据存储
# @app.on_event("startup")
# async def startup():
#     """aioredis"""
#     app.state.redis: Redis = await aioredis.from_url("redis://127.0.0.1:6379",  decode_responses=True)
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     """close redis"""
#     await app.state.redis.close()

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(fmt)

# will print debug sql
logger_db_client = logging.getLogger("db_client")
logger_db_client.setLevel(logging.DEBUG)
logger_db_client.addHandler(sh)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(sh)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    db_url="sqlite://menber_management.db",
    # db_url="mysql://root:root@192.168.87.132:3306/gccisc?charset=utf8mb4",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
