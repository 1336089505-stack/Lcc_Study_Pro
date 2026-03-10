import logging

from core.settings import setup_logging

def pytest_configure():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.debug("开始测试......")