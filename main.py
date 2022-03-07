import SQL
import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md
import parse






async def on_startup(_):
    SQL.sql_start()
    parse.parse()



storage = MemoryStorage()
bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=storage)


class Test(StatesGroup):
    name = State()
    zodiac = State()


@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await Test.name.set()
    await message.reply('Введи своё имя')


@dp.message_handler(state=Test.name)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await Test.next()
        await message.reply('Какой у вас знак зодиака?')


@dp.message_handler(state=Test.zodiac)
async def get_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['zodiac'] = message.text

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Привет, рад знакомству,', data['name']),
                md.text('Знак зодиака:', data['zodiac']),

                sep='\n'
            ),

        )
    await SQL.sql_add_command(state)
    await state.finish()





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


















