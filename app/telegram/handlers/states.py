from aiogram.dispatcher.filters.state import State, StatesGroup


class MenuSG(StatesGroup):
    start = State()
    dates_diff = State()
    days_for = State()
    last_date = State()


class DatesDiffSG(StatesGroup):
    start = State()
    last_date = State()


class LastDateSG(StatesGroup):
    start = State()
    days = State()