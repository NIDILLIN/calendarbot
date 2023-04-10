from app.telegram.handlers.text.menu.dates_diff import reg_dates_diff_handler
from app.telegram.handlers.text.menu.last_date import reg_last_date_handler


def reg_menu(dp):
    reg_dates_diff_handler(dp)
    reg_last_date_handler(dp)