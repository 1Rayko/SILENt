if apt --help;then
	clear
	echo "Apt найден"
	sudo apt install python -y
else
	echo"Apt не найден"
fi

if pkg --help;then
	clear 
	echo "Pkg найден"
	pkg install python -y

else
	echo "Pkg не найден"
fi

if pacman --help;then
	clear
	echo "Pacman найден"
	sudo pacman -Sy python python-pip --noconfirm 
else
	echo "Pacman не найден"
fi
python3 -m pip install pyTelegramBotAPI==0.3.0
python3 -m pip install pyautogui
python3 -m pip install opencv-python
python3 -m pip install colorama
python3 -m pip install random
clear
echo "Установка зависимостей завершена, следуйте инструкциям далее"
