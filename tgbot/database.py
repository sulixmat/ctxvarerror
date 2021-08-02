import logging

import aiomysql

from .config import load_config

logger = logging.getLogger(__name__)


async def connect() -> aiomysql.Connection:
    config = load_config('bot.ini')
    try:
        return await aiomysql.connect(
            user=config.db.user,
            password=config.db.password,
            db=config.db.database,
            host=config.db.host,
            charset='utf8mb4',
            cursorclass=aiomysql.cursors.DictCursor,
        )
    except Exception as e:
        logger.exception('error when connection to DB:', e)
        raise NotImplementedError
