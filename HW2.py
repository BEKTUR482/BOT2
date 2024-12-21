import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher()

buttons = [
     [KeyboardButton(text='Новости'), KeyboardButton(text='Курсы валют')],
     [KeyboardButton(text='Контактная информация'), KeyboardButton(text='Часто задаваемые вопросы (FAQ)')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Доступные команды:\n"
                         "/start - Начать взаимодействие с ботом\n"
                         "/help - Получить описание доступных функций\n"
                         "/about - Узнать о проекте\n"
                         "/menu - Вернуться в основное меню")
    await message.answer("Привет! Я бот, который предоставляет информацию на разные темы.\n\n"
                         "Выберите одну из тем ниже:", reply_markup=keyboard)

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("Доступные команды:\n"
                         "/start - Начать взаимодействие с ботом\n"
                         "/help - Получить описание доступных функций\n"
                         "/about - Узнать о проекте\n"
                         "/menu - Вернуться в основное меню")

@dp.message(Command('about'))
async def about_command(message: types.Message):
    await message.answer("Этот бот предоставляет информацию по различным темам: новости, курсы валют, контактные данные и ответы на часто задаваемые вопросы.\n"
                         "Бот создан для удобного получения информации и быстрого взаимодействия с пользователями.")

@dp.message(Command('menu'))
async def menu_command(message: types.Message):  
    await message.answer("Выберите одну из тем ниже:", reply_markup=keyboard)


@dp.message(F.text=="Новости")
async def show_news(message: types.Message):
    news_text = "Сегодня: курс доллара вырос на 2%, акции падают."
    await message.answer(news_text)

@dp.message(F.text=="Курсы валют")
async def show_exchange_rates(message: types.Message):
    exchange_rates = "Доллар: 85₽, Евро: 90₽."
    await message.answer(exchange_rates)

@dp.message(F.text=="Контактная информация")
async def show_contacts(message: types.Message):
    contacts = "Наша почта: info@example.com. Телефон: +123456789."
    await message.answer(contacts)

@dp.message(F.text=="Часто задаваемые вопросы (FAQ)")
async def show_faq(message: types.Message):
    faq = "Q: Как получить информацию?\nA: Просто выбери тему из меню.\n\n"
    faq += "Q: Как связаться с нами?\nA: Используй контактные данные в меню."
    await message.answer(faq)


async def main():
        await dp.start_polling(bot)
if __name__=='__main__':
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')

