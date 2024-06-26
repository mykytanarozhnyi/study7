from aiogram import Bot, Dispatcher, F, types
import asyncio
from aiogram.filters.command import Command
from aiogram.enums import ParseMode

bot = Bot(token="7391481973:AAH5VOeFllAuq1yyumo7y5yc6qc50E3kASk")

dispatcher = Dispatcher()
@dispatcher.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="котик")],

        [types.KeyboardButton(text="собачка")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Котик или собачка?", reply_markup=keyboard)

@dispatcher.message(F.text == "котик")
async def handle_cat(message):
    await message.answer("https://vet-centre.by/wp-content/uploads/2016/11/kot-eti-udivitelnye-kotiki.jpg")

@dispatcher.message(F.text == "собачка")
async def handle_dog(message):
    await message.answer("https://cn15.nevsedoma.com.ua/photo/12/1218/110_files/pembroke-welsh-corgi-vancouver-1.jpg")

@dispatcher.message(Command("start"))
async def handle_start(message):
    await message.answer("Привет, 100 котлет")

@dispatcher.message(F.text == "hello")
async def handle_unknown(message):
    await message.answer("Hello!")

@dispatcher.message(F.text == "HELLO!!!")
async def handle_expressive(message: types.Message):
    await message.answer(
        f"Hello,<i>{message.from_user.first_name}!</i>",
        parse_mode=ParseMode.HTML
    )



@dispatcher.message(F.text)
async def handle_unknown(message):
    await message.answer("Не понимаю что ты хочешь, выбери другое")

async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())