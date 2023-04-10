from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from app.telegram.handlers.states import MenuSG, DatesDiffSG, LastDateSG


async def cmd_menu(message: types.Message, state: FSMContext):
    await state.finish()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Разница между датами'))
    # keyboard.add(types.KeyboardButton('Количество дней от/до даты'))
    keyboard.add(types.KeyboardButton('Узнать конечную дату'))
    await message.reply(
        'Меню',
        reply_markup=keyboard
    )
    await state.set_state(MenuSG.start.state)


def reg_menu_cmd(dp: Dispatcher):
    dp.register_message_handler(cmd_menu, commands='menu', state='*')
    dp.register_message_handler(cmd_menu, Text('назад', ignore_case=True), state=DatesDiffSG.start)
    dp.register_message_handler(cmd_menu, Text('назад', ignore_case=True), state=LastDateSG.start)
