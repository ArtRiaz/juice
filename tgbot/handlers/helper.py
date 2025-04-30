from aiogram import Router, F, Bot, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from tgbot.config import load_config
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from tgbot.keyboards.inline import main_menu, order_set
from data_example.data import catalog_items_sets
import random

config = load_config(".env")

helper_router = Router()

photo = FSInputFile("tgbot/logo.png")


class JuiceOrderStates(StatesGroup):
    one = State()
    two = State()
    three = State()


@helper_router.callback_query(F.data == "start_order")
async def helper(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(JuiceOrderStates.one)

    text = "Take our questionnaire and get our recommendations\n" \
           "First question:"
    await callback.answer()
    await callback.message.answer_photo(photo, text)


@helper_router.message(StateFilter(JuiceOrderStates.one))
async def one_ques(message: types.Message, state: FSMContext):
    await state.update_data(one=message.text)
    await state.set_state(JuiceOrderStates.two)

    text = "Second question:"

    await message.answer(text)


@helper_router.message(StateFilter(JuiceOrderStates.two))
async def two_ques(message: types.Message, state: FSMContext):
    await state.update_data(two=message.text)
    await state.set_state(JuiceOrderStates.three)

    text = "Third question:"

    await message.answer(text)


@helper_router.message(StateFilter(JuiceOrderStates.three))
async def three_ques(message: types.Message, state: FSMContext):
    await state.update_data(three=message.text)
    data = await state.get_data()
    print(f"{data['one']}\n{data['two']}\n{data['three']}")

    jucie = [
        "Detox Deep – Deep Body Cleanse",
        "Mind & Body Balance"
    ]

    await message.answer(f"Recomendation for you\n{random.choice(jucie)}", reply_markup=order_set())
    await state.clear()
