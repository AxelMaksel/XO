from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from handlers.users.game import board


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="=", callback_data="move:0"),
            InlineKeyboardButton(text="=", callback_data="move:1"),
            InlineKeyboardButton(text="=", callback_data="move:2"),

        ],
        [
            InlineKeyboardButton(text="=", callback_data="move:3"),
            InlineKeyboardButton(text="=", callback_data="move:4"),
            InlineKeyboardButton(text="=", callback_data="move:5"),

        ],
        [
            InlineKeyboardButton(text="=", callback_data="move:6"),
            InlineKeyboardButton(text="=", callback_data="move:7"),
            InlineKeyboardButton(text="=", callback_data="move:8"),

        ],

    ]
)
