from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from tgbot.config import load_config
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from tgbot.keyboards.inline import main_menu, back

config = load_config(".env")

about_router = Router()

photo = FSInputFile("tgbot/logo.png")


@about_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    text = "Our Story\n\nWelcome to Koh Phangan Juice Bar, where tropical paradise meets wellness!Nestled on the " \
           "beautiful island of Koh Phangan, our juice bar was born from a simple yet powerful vision: to harness the " \
           "islands abundant natural resources and create delicious, nutrient-rich juices that support health, " \
           "vitality, and wellbeing.\n\n" \
           "Our Philosophy\n\n" \
           "We believe that what you put into your body matters. Our philosophy is centered around three core " \
           "principles:\n\n" \
           "✅ Organic & Local: We source our fruits and vegetables directly from local organic farms on Koh Phangan " \
           "and " \
           "neighboring islands, ensuring maximum freshness and supporting the local community.\n\n" \
           "✅ Nutrient Preservation: Using cold-press technology, we extract juice in a way that preserves essential " \
           "enzymes, vitamins, and minerals that are often lost in conventional juicing methods.\n\n" \
           "✅ Sustainable Practices: From our eco-friendly packaging to our zero-waste initiatives, we're committed to " \
           "caring for the island that gives us so much beauty and abundance."
    await callback.answer()
    await callback.message.answer_photo(photo, text, reply_markup=back())


