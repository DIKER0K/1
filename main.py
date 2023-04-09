from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from revChatGPT.V3 import Chatbot
import logging
import os
import asyncio

print('Бот запущен!')

logging.basicConfig(level=logging.INFO)

chatbot = Chatbot(api_key="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")
TOKEN = token ='5747127396:AAEXYrvUMht9LJqUzxoQA-Xg4Tv8wO98tRI'

router = Router()

@router.message(Command(commands=["clear"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(text='История очищена!')
    chatbot.reset()


@router.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer( text='Обрабатываю запрос, пожалуйста подождите!')
    result = chatbot.ask(message.text)
    await message.answer(text=result)

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

