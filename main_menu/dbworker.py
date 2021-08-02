import logging

import aiomysql

logger = logging.getLogger(__name__)

async def add_user(connection: aiomysql.Connection, telegram_id):
    cursor = await connection.cursor()
    await cursor.execute('INSERT INTO users(telegram_id, username) values (%s, "anydata")', telegram_id)
    await connection.commit()


async def main_category_list(connection: aiomysql.Connection):
    cursor = await connection.cursor()
    await cursor.execute('SELECT * from main_category')
    return await cursor.fetchall()