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
from data_example.data import catalog_items, catalog_items_sets

config = load_config(".env")

catalog_router = Router()

photo = FSInputFile("tgbot/logo.png")


@catalog_router.callback_query(F.data == "view_menu")
async def catalog(callback: types.CallbackQuery):
    await callback.answer()

    catalog_text = (
        "🥤 Catalog\n\n"
        "Choose a category to explore our juice offerings:"
    )
    await callback.message.answer_photo(photo, catalog_text, reply_markup=main_catalog())


# CallbackData для управления пагинацией
class PaginationCallback(CallbackData, prefix="pagination"):
    action: str  # "left" или "right"
    page: int  # Номер страницы


# Функция для генерации клавиатуры пагинации
def pagination_keyboard(current_page: int, total_pages: int):
    navigation_buttons = []

    if current_page > 0:
        navigation_buttons.append(
            InlineKeyboardButton(
                text="Back ⏪",
                callback_data=PaginationCallback(action="left", page=current_page - 1).pack()
            )
        )
    if current_page < total_pages - 1:
        navigation_buttons.append(
            InlineKeyboardButton(
                text="Next ⏩",
                callback_data=PaginationCallback(action="right", page=current_page + 1).pack()
            )
        )

    return InlineKeyboardMarkup(
        inline_keyboard=[
            navigation_buttons,
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


# Обработчик начального каталога
@catalog_router.callback_query(F.data == "catalog_juices")
async def show_catalog(callback_query: types.CallbackQuery):
    page = 0  # Начальная страница
    await send_catalog_page(callback_query.message, page)
    await callback_query.answer()


# Обработчик пагинации juice
@catalog_router.callback_query(PaginationCallback.filter())
async def paginate_catalog(callback_query: types.CallbackQuery, callback_data: PaginationCallback):
    page = callback_data.page  # Получаем текущую страницу из callback_data
    await send_catalog_page(callback_query.message, page)
    await callback_query.answer()


# Функция для отправки страницы каталога juice
async def send_catalog_page(message: types.Message, page: int):
    total_pages = len(catalog_items)
    item = catalog_items[page]
    keyboard = pagination_keyboard(page, total_pages)
    # Обновляем сообщение с новым контентом
    await message.edit_media(
        media=types.InputMediaPhoto(media=FSInputFile(item["photo"]), caption=item["caption"]),
        reply_markup=keyboard
    )



