from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from tgbot.config import load_config
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from tgbot.keyboards.inline import main_menu, support_kb

config = load_config(".env")

contact_us_router = Router()

photo = FSInputFile("tgbot/logo.png")


@contact_us_router.callback_query(F.data == "support")
async def contact(callback: types.CallbackQuery):
    text = "Do you need support?\n" \
           "Click here and write message 👇"

    await callback.answer()
    await callback.message.answer_photo(photo, text, reply_markup=support_kb())

