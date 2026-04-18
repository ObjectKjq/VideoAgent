"""FastAPI 主应用入口"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.database import engine, Base
from app.routers.user_router import user_router
from app.exceptions import BusinessException, ErrorCode


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    Base.metadata.create_all(bind=engine)
    print(f"数据库连接成功: {settings.database_url}")
    yield
    print("应用已关闭")

# 创建 FastAPI 应用
app = FastAPI(
    title="AI 视频生成器",
    description="AI 视频生成器 - Python 后端",
    version="0.0.1",
    lifespan=lifespan
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 前端开发服务器地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 全局异常处理
@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    """业务异常处理"""
    return JSONResponse(
        status_code=200,
        content={
            "code": exc.error_code.code,
            "data": None,
            "message": exc.message
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """全局异常处理"""
    print(f"未处理的异常: {exc}")
    return JSONResponse(
        status_code=200,
        content={
            "code": ErrorCode.SYSTEM_ERROR.code,
            "data": None,
            "message": f"系统内部异常: {str(exc)}"
        }
    )


app.include_router(user_router, prefix="/api")
