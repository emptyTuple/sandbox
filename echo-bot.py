from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram import F
import requests
import os

bot = Bot(token=os.getenv("EMPTY_TOKEN"))
dp = Dispatcher()

async def handle_start(message: Message):
    print(message.model_dump_json(indent=2, exclude_none=True))
    await message.answer("Hello, I am echo bot.")

async def handle_help(message: Message):
    await message.answer("What could I help you with?")

async def handle_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def handle_sticker(message: Message):
    await message.reply_sticker(message.sticker.file_id)

async def send_echo (message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply("I can't echo this message")



if __name__ == "__main__":
    dp.message.register(handle_start, Command("start"))
    dp.message.register(handle_help, Command("help"))
    dp.message.register(handle_photo, F.photo)
    dp.message.register(handle_sticker, F.sticker)
    dp.message.register(send_echo)
    dp.run_polling(bot)

