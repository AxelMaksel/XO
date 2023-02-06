from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import action_callback
from keyboards.inline.choice_buttons import move
# from keyboards.inline.choice_buttons import choice
from loader import dp, logger
from mod_calc import sum_data, sub_data, mul_data, div_data

nums = ""
# board = list(range(1, 10))
board = list("❤❤❤❤❤❤❤❤❤")
counter = 0



@dp.message_handler(Command("start"))
async def show_field(message: Message):
    await message.answer(text="Let's calculate",
                         reply_markup=move(board))


# @dp.callback_query_handler(text_contains="<")
# async def delete_char(call: CallbackQuery):
#     global nums
#     if nums:
#         nums = nums[:-1]
#         if not nums:
#             await call.message.edit_text("0", reply_markup=move(board))
#         await call.message.edit_text(f"{nums}", reply_markup=move(board))
#     else:
#         await call.answer(cache_time=20)


# @dp.callback_query_handler(text_contains="C")
# async def erase(call: CallbackQuery):
#     global nums
#     nums = ""
#     await call.message.edit_text("0", reply_markup=move(board))


@dp.callback_query_handler(action_callback.filter())
async def nums_choice(call: CallbackQuery, callback_data: dict):
    global nums, board

    await call.answer(cache_time=1)
    data = callback_data["item_name"]
    nums += data
    # idata = int(data)
    print(data)
    print(type(data))
    # print(type(idata),idata**3)
    board[int(data)] = "X"
    logger.debug(f"Ход: {counter}, board: {board}")
    await call.message.edit_text(f"{nums}", reply_markup=move(board))
    logger.debug(f'Пользователь ввел {nums}')


