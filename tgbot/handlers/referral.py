from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import FSInputFile
from tgbot.config import load_config
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from tgbot.keyboards.inline import main_menu, referral_menu

config = load_config(".env")

referral_router = Router()

photo = FSInputFile("tgbot/logo.png")


@referral_router.callback_query(F.data == "invite_friend")
async def referral(callback: types.CallbackQuery):
    text = "Share the Juice\n\n Love believe that wellness is better when shared with friends! Our referral program " \
           "lets " \
           "you spread the goodness of fresh, organic juices while earning rewards for yourself.\n\n" \
           "How It Works\n\n1.Share with FriendsSend your unique referral link to friends who are visiting or living " \
           "on Koh Phangan. Tell them about your favorite juices and why you love our service!\n\n" \
           "2. Friends Place Their First Order\n\nWhen your friends place their first order, they'll be asked to enter " \
           "your referral code or phone number.\n\n" \
           "3. Everyone Wins!\n\nYou receive: 10% OFF your next order for each friend who makes their first " \
           "purchase\nYour friend receives: 5% OFF their first order\nBonuses stack: Refer 10 friends and get a FREE " \
           "juice set of your choice!"

    await callback.answer()
    await callback.message.answer_photo(photo, text, reply_markup=referral_menu())


@referral_router.callback_query(F.data == "statistic")
async def statistics(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    friendship = 3
    bonuses = 10
    await callback.message.answer(f"🔥 Your Referral Stats! 🔥\n\n"
                                  f"👥 Invited Friends:  {friendship}\n\n"
                                  f"💰 Earned Bonuses:  {bonuses} ")


@referral_router.callback_query(F.data == "create_link")
async def link(callback: types.CallbackQuery):
    user = callback.from_user.id
    referral_link = f"https://t.me/juicypussy_freshbot?start={user}"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Invite Link",
                                  switch_inline_query=f"🔥 text"
                                                      f"Join us: {referral_link}")]
        ]
    )

    await callback.message.answer(
        f"🔗 Your referral link:\n{referral_link}\n\n"
        "📢 Click here",
        reply_markup=keyboard
    )



