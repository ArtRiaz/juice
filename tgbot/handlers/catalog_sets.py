from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from tgbot.config import load_config
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from tgbot.keyboards.inline import main_catalog
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from data_example.data import catalog_items_sets

config = load_config(".env")

catalog_set_router = Router()

photo = FSInputFile("tgbot/logo.png")


# CallbackData для управления пагинацией
class PaginationCallback(CallbackData, prefix="pagination_set"):
    action: str  # "left" или "right"
    page: int  # Номер страницы


# Функция для генерации клавиатуры пагинации
def pagination_keyboard(current_page: int, total_pages: int):
    navigation_buttons_set = []

    if current_page > 0:
        navigation_buttons_set.append(
            InlineKeyboardButton(
                text="Back ⏪",
                callback_data=PaginationCallback(action="left", page=current_page - 1).pack()
            )
        )
    if current_page < total_pages - 1:
        navigation_buttons_set.append(
            InlineKeyboardButton(
                text="Next ⏩",
                callback_data=PaginationCallback(action="right", page=current_page + 1).pack()
            )
        )

    return InlineKeyboardMarkup(
        inline_keyboard=[
            navigation_buttons_set,
            [InlineKeyboardButton(
                text="🛒 Add to cart",
                callback_data="add_cart"
            )],
            # Кнопки навигации на первой строке
            [
                InlineKeyboardButton(
                    text="↩️ Back main menu",
                    callback_data="back_main"
                )
            ]  # Кнопка "Назад" на отдельной строке
        ]
    )


@catalog_set_router.callback_query(F.data == "catalog_sets")
async def show_catalog_sets(callback_query: types.CallbackQuery):
    page = 0  # Начальная страница
    await send_catalog_page_sets(callback_query.message, page)
    await callback_query.answer()


# Функция для отправки страницы каталога sets
async def send_catalog_page_sets(message: types.Message, page: int):
    total_pages = len(catalog_items_sets)
    item = catalog_items_sets[page]
    keyboard = pagination_keyboard(page, total_pages)
    # Обновляем сообщение с новым контентом
    await message.edit_media(
        media=types.InputMediaPhoto(media=FSInputFile(item["photo"]), caption=item["caption"]),
        reply_markup=keyboard
    )


# пагинация sets
@catalog_set_router.callback_query(PaginationCallback.filter())
async def paginate_catalog(callback_query: types.CallbackQuery, callback_data: PaginationCallback):
    page = callback_data.page  # Получаем текущую страницу из callback_data
    await send_catalog_page_sets(callback_query.message, page)
    await callback_query.answer()
