from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from handlers.users.game import board


def move(board):
    choice = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=board[0], callback_data="move:0"),
                InlineKeyboardButton(text=board[1], callback_data="move:1"),
                InlineKeyboardButton(text=board[2], callback_data="move:2"),

            ],
            [
                InlineKeyboardButton(text=board[3], callback_data="move:3"),
                InlineKeyboardButton(text=board[4], callback_data="move:4"),
                InlineKeyboardButton(text=board[5], callback_data="move:5"),

            ],
            [
                InlineKeyboardButton(text=board[6], callback_data="move:6"),
                InlineKeyboardButton(text=board[7], callback_data="move:7"),
                InlineKeyboardButton(text=board[8], callback_data="move:8"),

            ],

        ]
    )

    return choice