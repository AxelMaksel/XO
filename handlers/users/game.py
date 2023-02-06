from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import action_callback
from keyboards.inline.choice_buttons import move
from loader import dp, logger

nums = ""
# board = list(range(0, 9))
board = list("▫▫▫▫▫▫▫▫▫")
counter = 0


@dp.message_handler(Command("start"))
async def show_field(message: Message):
    global board
    board = list("▫▫▫▫▫▫▫▫▫")
    await message.answer(text="Game X-O !!! Go...",
                         reply_markup=move(board))
    


@dp.callback_query_handler(action_callback.filter())
async def nums_choice(call: CallbackQuery, callback_data: dict):
    global nums, board
    global counter
    await call.answer(cache_time=1)
    data = callback_data["item_name"]
    nums += data
    # board[int(data)] = "X"
    if board[int(data)] == "▫":
        if counter % 2 == 0:
            board[int(data)] = "❌"
        else:
            board[int(data)] = "⭕"
        counter += 1
        if counter > 4:
            tmp = await check_win(board)
            if tmp:
                # print(tmp, "выиграл!")
                await call.message.answer(f"{tmp}, выиграл!")
        if counter == 9:
            await call.message.answer(f"НИЧЬЯ!")

    logger.debug(f"Ход: {counter}, board: {board}")
    await call.message.edit_text(f"{nums}", reply_markup=move(board))
    logger.debug(f'Пользователь ввел {nums}')


async def check_win(boar):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if boar[each[0]] == boar[each[1]] == boar[each[2]] != "▫":
            return boar[each[0]]
    return False
