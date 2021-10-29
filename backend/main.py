from uvicorn import run
from api import app

if __name__ == '__main__':
    # reload代码有更改自动启动 debug模式 workers进程数量
    # dev
    print(__name__)
    run(app=f'main:app', port=5000, host='0.0.0.0', reload=True)
