import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import config
from aiogram.types import CallbackQuery

API_TOKEN = config.TOKEN

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)