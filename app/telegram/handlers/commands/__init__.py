from app.telegram.handlers.commands.start import reg_start_cmd
from app.telegram.handlers.commands.menu import reg_menu_cmd


def reg_commands(dp):
    reg_start_cmd(dp)
    reg_menu_cmd(dp)