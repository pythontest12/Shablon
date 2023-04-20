from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from states.holatlar import Tanlov
from keyboards.default.menu_uchun import menu_buttons


from loader import dp,base


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)


menular = base.select_all_menu()
print(menular)
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    menu_nomi = message.text
    tanlangan_menu= base.select_mahsulot(tur=menu_nomi)
    print(tanlangan_menu)
    index = 0
    keys = []
    j = 0
    for menu in tanlangan_menu:
        print(menu,"******************")
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f"{menu[0]}", )])
        else:
            keys[index].append(KeyboardButton(text=f"{menu[0]}", ))
        j += 1
    keys.append([KeyboardButton(text='Ortga')])
    menu_buttons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)
    await Tanlov.mahsulot_tanlash_holati.set()

    @dp.message_handler(text='', state=Tanlov.mahsulot_tanlash_holati)
    async def bot_start(message: types.Message):
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)

