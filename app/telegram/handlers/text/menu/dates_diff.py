from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.core.calendar import Converter, Calculator

from app.telegram.handlers.text.menu import common
from app.telegram.handlers.states import MenuSG, DatesDiffSG


norm = Converter.normalize


async def dates_diff(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Назад'))
    await message.reply(
        '<b>ИНСТРУМЕНТ | ДЕЛЬТА</b>\n'
        +'Подсчитывает количество дней между двумя датами.\n'
        +'Чтобы начать, напиши первую дату, или нажми кнопку НАЗАД',
        reply_markup=keyboard
    )
    await state.set_state(DatesDiffSG.start.state)


async def dd_first_date(message: types.Message, state: FSMContext):
    text = message.text
    first_date = Converter.convert(text)
    await state.update_data(first_date=first_date)

    await message.reply(
        f'Первая дата -- <b><i>{norm(first_date)}</i></b>\n'
        +'Напиши вторую:'

    )
    await state.set_state(DatesDiffSG.last_date.state)


async def dd_last_date(message: types.Message, state: FSMContext):
    text = message.text
    last_date = Converter.convert(text)
    data = await state.get_data()
    first_date = data['first_date']

    delta = Calculator.calc_diff(first_date, last_date)
    await message.reply(
        f'Разница между <b><i>{norm(first_date)}</i></b> и <b><i>{norm(last_date)}</i></b> составляет:\n'
        +f'<b>{delta}</b> дней'
    )
    await state.finish()
    await common.cmd_menu(message, state)


def reg_dates_diff_handler(dp: Dispatcher):
    dp.register_message_handler(
        dates_diff, 
        Text(equals='разница между датами', ignore_case=True), 
        state=MenuSG.start
    )
    dp.register_message_handler(
        dd_first_date,
        content_types='text',
        state=DatesDiffSG.start
    )
    dp.register_message_handler(
        dd_last_date,
        state=DatesDiffSG.last_date
    )
    