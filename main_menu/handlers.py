import logging
from typing import Union

from aiogram.dispatcher.dispatcher import Dispatcher
import aiogram.utils.markdown as fmt
from aiogram import types

from tgbot.database import connect
from .keyboards import main_keyboard_kb 
from main_menu.dbworker import add_user

logger = logging.getLogger(__name__)


def main_munu_register(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start'])


async def start_cmd(message: Union[types.CallbackQuery, types.Message], **kwargs):
    if isinstance(message, types.Message):        
        chat_id = message.chat.id
    elif isinstance(message, types.CallbackQuery):  
        chat_id = message.message.chat.id
        message = message.message
    
    connection = await connect()
    await add_user(connection, chat_id)
    markup = await main_keyboard_kb(connection)

    await message.reply(
        reply=False,
        reply_markup=markup,
        disable_notification=True,
        text=fmt.hbold('Категории главного меню')
        )
    connection.close()
