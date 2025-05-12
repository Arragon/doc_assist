from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 验证环境变量
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY 环境变量未设置")

# 创建FastAPI应用
app = FastAPI(title="文档AI助手", description="基于AI的文档智能助手")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应限制为前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 测试路由
@app.get("/")
async def root():
    return {"message": "文档AI助手API已启动"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# 启动服务器（仅在直接运行此文件时）
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

