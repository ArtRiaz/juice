from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def main_menu():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="🥤 Catalog", web_app=WebAppInfo(url="https://example.com")))
    builder.add(InlineKeyboardButton(text="ℹ️ About", callback_data="about"))
    builder.add(InlineKeyboardButton(text="👥 Invite a Friend", callback_data="invite_friend"))
    builder.add(InlineKeyboardButton(text="📋 Contacts", callback_data="contacts"))
    builder.adjust(1)
    return builder.as_markup()


def main_catalog():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="🧃 Juices", callback_data="catalog_juices"))
    builder.add(InlineKeyboardButton(text="🔢 Sets", callback_data="catalog_sets"))
    builder.add(InlineKeyboardButton(text="🔙 Back to Menu", callback_data="back_main"))
    builder.adjust(1)
    return builder.as_markup()


def back():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="↩️ Back to main menu", callback_data="back_main"))
    builder.adjust(1)
    return builder.as_markup()


def referral_menu():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="📈 Statistic", callback_data="statistic"))
    builder.add(InlineKeyboardButton(text="🔗 Create Link", callback_data="create_link"))
    builder.add(InlineKeyboardButton(text="↩️ Back to main menu", callback_data="back_main"))
    builder.adjust(1)
    return builder.as_markup()


def social():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Instagram", url="https://instagram.com"))
    builder.add(InlineKeyboardButton(text="E-mail", callback_data="email"))
    builder.add(InlineKeyboardButton(text="What's app", callback_data="whatsapp"))
    builder.add(InlineKeyboardButton(text="↩️ Back to main menu", callback_data="back_main"))
    builder.adjust(1)
    return builder.as_markup()


def support_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Contact with us", url="https://t.me/ArtemRiaz22"))
    builder.add(InlineKeyboardButton(text="↩️ Back to main menu", callback_data="back_main"))
    builder.adjust(1)
    return builder.as_markup()


def order_set():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Order Set", callback_data="catalog_sets"))
    builder.add(InlineKeyboardButton(text="↩️ Back to main menu", callback_data="back_main"))
    builder.adjust(1)
    return builder.as_markup()
