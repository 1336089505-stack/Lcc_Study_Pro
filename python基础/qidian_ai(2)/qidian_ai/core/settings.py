import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
import logging

# 环境变量的绝对路径
load_dotenv()
ENV = os.getenv("ENVIRONMENT")  #, "dev"
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / f".env.{ENV}"

class Config(BaseSettings):

    # ============ 项目配置 ============
    DEBUG: bool = True
    PROJECT_NAME: str = "QiDian Ai"
    VERSION: str = "1.0.0"

    # ============ 服务器配置 ============
    HOST: str = "0.0.0.0"
    PORT: int = 80
    RELOAD: bool = True
    WORKERS: int = 1  # 添加缺失的字段

    # ============ 数据库配置 ============
    DATABASE_URL: str = ""
    DATABASE_ECHO: bool = True
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 5

    # ============ 其它配置 ============
    # 日志
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"


    # 自动根据环境变量选择配置文件
    model_config = SettingsConfigDict(
        env_file = ENV_FILE,  #这里路径不对则无法加载到配置
        env_file_encoding = "utf-8",
        case_sensitive = False,
        extra = "ignore"
    )

config = Config()

def setup_logging():
    """
    初始化日志
    :return:
    """
    logging.basicConfig(
        level = getattr(logging, config.LOG_LEVEL),  #这是把字符串 → logging 常量的标准做法。
        format = '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S'
    )
