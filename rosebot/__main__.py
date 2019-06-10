import sys
import importlib

from rosebot.modules import ALL_MODULES
from rosebot import BOT, LOGS


for module_name in ALL_MODULES:
    imported_module = importlib.import_module("rosebot.modules." + module_name)


if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    BOT.start()
    BOT.idle()
