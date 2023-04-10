from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.core.calendar import Converter, Calculator

from app.telegram.handlers.text.menu import common
from app.telegram.handlers.states import MenuSG, LastDateSG


norm = Converter.normalize


async def last_date(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Назад'))
    await message.reply(
        '<b>ИНСТРУМЕНТ | КОНЕЧНАЯ ДАТА</b>\n'
        +'Подсчитывает дату спустя заданное количество дней.\n'
        +'Чтобы начать, напиши дату, или нажми кнопку НАЗАД',
        reply_markup=keyboard
    )
    await state.set_state(LastDateSG.start.state)


async def ld_first_date(message: types.Message, state: FSMContext):
    text = message.text
    first_date = Converter.convert(text)
    await state.update_data(first_date=first_date)

    await message.reply(
        f'Первая дата -- <b><i>{norm(first_date)}</i></b>\n'
        +'Напиши количество дней одним числом:'

    )
    await state.set_state(LastDateSG.days.state)


async def ld_days(message: types.Message, state: FSMContext):
    text = message.text
    days = int(text)
    data = await state.get_data()
    first_date = data['first_date']

    date = Calculator.calc_last_date(first_date, days)
    await message.reply(
        f'<b><i>{norm(first_date)}</i></b> + <b><i>{days}</i></b> дней:\n'
        +f'<b>{norm(date)}</b>'
    )
    await state.finish()
    await common.cmd_menu(message, state)


def reg_last_date_handler(dp: Dispatcher):
    dp.register_message_handler(
        last_date, 
        Text(equals='узнать конечную дату', ignore_case=True), 
        state=MenuSG.start
    )
    dp.register_message_handler(
        ld_first_date,
        state=LastDateSG.start
    )
    dp.register_message_handler(
        ld_days,
        state=LastDateSG.days
    )
    