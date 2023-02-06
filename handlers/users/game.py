from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import action_callback
# from keyboards.inline.choice_buttons import choice
from loader import dp, logger
from mod_calc import sum_data, sub_data, mul_data, div_data

nums = ""
# board = list(range(1, 10))
board = list("❤❤❤❤❤❤❤❤❤")
counter = 0

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=board[0], callback_data="move:1"),
            InlineKeyboardButton(text=board[1], callback_data="move:2"),
            InlineKeyboardButton(text=board[2], callback_data="move:3"),

        ],
        [
            InlineKeyboardButton(text=board[3], callback_data="move:4"),
            InlineKeyboardButton(text=board[4], callback_data="move:5"),
            InlineKeyboardButton(text=board[5], callback_data="move:6"),

        ],
        [
            InlineKeyboardButton(text=board[6], callback_data="move:7"),
            InlineKeyboardButton(text=board[7], callback_data="move:8"),
            InlineKeyboardButton(text=board[8], callback_data="move:9"),

        ],

    ]
)


@dp.message_handler(Command("start"))
async def show_field(message: Message):
    await message.answer(text="Let's calculate",
                         reply_markup=choice)


@dp.callback_query_handler(text_contains="<")
async def delete_char(call: CallbackQuery):
    global nums
    if nums:
        nums = nums[:-1]
        if not nums:
            await call.message.edit_text("0", reply_markup=choice)
        await call.message.edit_text(f"{nums}", reply_markup=choice)
    else:
        await call.answer(cache_time=20)


@dp.callback_query_handler(text_contains="C")
async def erase(call: CallbackQuery):
    global nums
    nums = ""
    await call.message.edit_text("0", reply_markup=choice)


@dp.callback_query_handler(action_callback.filter())
async def nums_choice(call: CallbackQuery, callback_data: dict):
    global nums

    await call.answer(cache_time=1)
    data = callback_data["item_name"]
    nums += data
    idata = int(data)
    print(type(idata),idata**3)
    board[idata] = "X"
    logger.debug(f"Ход: {counter}, board: {board}")
    await call.message.edit_text(f"{nums}", reply_markup=choice)
    logger.debug(f'Пользователь ввел {nums}')


