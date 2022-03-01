import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.greet_kb)


@dp.message_handler(commands=['hi2'])
async def process_hi2_command(message: types.Message):
    await message.reply("Второе - прячем клавиатуру после одного нажатия", reply_markup=kb.greet_kb2)


@dp.message_handler(commands=['hi3'])
async def process_hi3_command(message: types.Message):
    await message.reply("Третье - добавляем больше кнопок", reply_markup=kb.markup3)


@dp.message_handler(commands=['hi4'])
async def process_hi4_command(message: types.Message):
    await message.reply("Четвертое - расставляем кнопки в ряд", reply_markup=kb.markup4)


@dp.message_handler(commands=['hi5'])
async def process_hi5_command(message: types.Message):
    await message.reply("Пятое - добавляем ряды кнопок", reply_markup=kb.markup5)

@dp.message_handler(commands=['hi6'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга", reply_markup=kb.markup_request)


@dp.message_handler(commands=['hi7'])
async def process_hi7_command(message: types.Message):
    await message.reply("Седьмое - все методы вместе", reply_markup=kb.markup_big)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений", reply_markup=kb.ReplyKeyboardRemove())
 
@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)

@dp.message_handler(lambda message: message.text == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


@dp.message_handler(lambda message: message.text=='btn')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code) 
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')

@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=kb.inline_kb_full)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)