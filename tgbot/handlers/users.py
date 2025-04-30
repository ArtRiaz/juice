from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from tgbot.config import load_config
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from tgbot.keyboards.inline import main_menu

config = load_config(".env")

user_router = Router()

photo = FSInputFile("tgbot/logo.png")

welcome_text = (
    "Welcome to Koh Phangan Juice Bar! 🌴\n\n"
    "We craft fresh, organic juices to help you feel your best during your stay on our beautiful island.\n\n"
    "Our personalized juice sets are designed to:\n"
    "✓ Boost your energy\n"
    "✓ Support detoxification\n"
    "✓ Enhance your immunity\n"
    "✓ Aid in fitness recovery\n\n"
    "Let me help you find the perfect juice set for your needs!"
)


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer_photo(photo, welcome_text, reply_markup=main_menu())


@user_router.callback_query(F.data == "back_main")
async def back(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo, welcome_text, reply_markup=main_menu())
