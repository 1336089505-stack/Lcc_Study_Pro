from core.settings import config, ENV_FILE
import logging

def test_get():
    print("ENV_FILE", ENV_FILE)
    print("DATABASE_URL", config.DATABASE_URL)
    print("DATABASE_POOL_SIZE", config.DATABASE_POOL_SIZE)
    print("DATABASE_MAX_OVERFLOW", config.DATABASE_MAX_OVERFLOW)


    logger = logging.getLogger(__name__)
    logger.error("DATABASE_MAX_OVERFLOW: %s", config.DATABASE_MAX_OVERFLOW)
    logger.info("DATABASE_URL: %s", config.DATABASE_URL)
    logger.debug("DATABASE_POOL_SIZE: %s", config.DATABASE_POOL_SIZE)
