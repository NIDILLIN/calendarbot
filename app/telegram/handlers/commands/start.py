from aiogram import types, Dispatcher


async def cmd_start(message: types.Message):
    await message.reply(
            "Привет! Я бот для калькуляции дат. "
            +"Я нужен, чтобы:\n"
            +" * Расчитать количество дней между датами\n"
            +" * Узнать дату по прошествии некоторого количества дней\n"
            +"И так далее)"
    )


def reg_start_cmd(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")