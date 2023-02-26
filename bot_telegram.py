from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
import asyncio
import datetime
import google_drive


import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)







@dp.message_handler(content_types=['voice'])
async def det_voice(message: types.Message):
    if message.chat.type == 'private':

        time = datetime.datetime.now()
        time = time.strftime("%m_%d_%Y__%H_%M_%S")

        file_id = message.voice.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        path_to_file = f"voice/{message.chat.username}/voice_{time}.mp3"  
        await bot.download_file(file_path, path_to_file)

        name = f"voice_{time}.mp3"
        folderName = str(message.chat.username) + '_' + str(message.from_user.id)
        try:
            m = google_drive.Sending_File(folderName, 'voice', path_to_file, name)
            await bot.send_message(message.from_user.id, f'Файл загружен на гугл диск:\n' + m.__dict__['link'])
        except:
            await bot.send_message(message.from_user.id, f'Ошибка загрузки файла')


    




@dp.message_handler(commands=['st']) 
async def command_start(message : types.Message): 
    m = google_drive.Sending_File('voice_3', 'voice_2', 'photo_25.png', 'some_file')
    #m.check('voice')
    #m()


    await bot.send_message(message.from_user.id, 'готово')
    await bot.send_message(message.from_user.id, m.__dict__)









executor.start_polling(dp, skip_updates=True) 

