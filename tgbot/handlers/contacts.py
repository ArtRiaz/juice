from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from tgbot.config import load_config
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from tgbot.keyboards.inline import main_menu, social

config = load_config(".env")

contacts_router = Router()

photo = FSInputFile("tgbot/logo.png")


@contacts_router.callback_query(F.data == "contacts")
async def contacts(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo, "Our social contacts:", reply_markup=social())


@contacts_router.callback_query(F.data == "whatsapp")
async def whats(callback: types.CallbackQuery):
    await callback.message.answer("Whats app number: +33762354721658")
    await callback.answer()
