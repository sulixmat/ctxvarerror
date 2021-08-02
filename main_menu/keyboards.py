from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from .dbworker import main_category_list


categories_callback_data = CallbackData('categories', 'step', 'level', 'category_id', 'sub_category_id', 'count')


def make_categories_callback_data(
    level, category_id=0,
    sub_category_id=0, step=0,
    count=0
):
    return categories_callback_data.new(
        level=level, category_id=category_id,
        sub_category_id=sub_category_id, step=step,
        count=count
    )


async def main_keyboard_kb(connection):
    CUR_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)
    categories = await main_category_list(connection)
    
    for item in categories:
        markup.row(
            InlineKeyboardButton(
                text=item['Name'],
                callback_data=make_categories_callback_data(
                    level=CUR_LEVEL+1,
                    category_id=item['id']
                )
            )
        )
    return markup