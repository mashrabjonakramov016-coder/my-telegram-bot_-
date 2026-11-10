import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# TOKEN yozilgan joyga @BotFather'dan olgan o'z tokeningizni tirnoq ichiga yozing
TOKEN = "9039662652:AAGGGpI7LHZ_aXWSywsXguizxgmm6YxDQt4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ Ma'lumot"), KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!\n"
        f"Botingiz muvaffaqiyatli ishga tushdi.",
        reply_markup=main_menu
    )

@dp.message(lambda msg: msg.text == "ℹ️ Ma'lumot")
async def info_handler(message: types.Message):
    await message.answer("Bu sizning Telegram botingiz!")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
