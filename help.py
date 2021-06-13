# coding: utf-8
#!/usr/bin/env python

__version__ = "v1.0"
__commands__ = "21"


from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Nemesis Selfbot v1.0 - Loading...")
print(
    f"""
{Fore.MAGENTA}
                                                ╔╗╔╔═╗╔╦╗╔═╗╔═╗╦╔═╗
                                                ║║║║╣ ║║║║╣ ╚═╗║╚═╗ {Fore.LIGHTMAGENTA_EX}
                                                ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═╝ 

                                                {Fore.WHITE}    Loading...


""")
print(f"{Fore.MAGENTA}")
progressbar = tqdm([1,2,3,4,5,6,7,9,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')
from discord.ext import commands
import json

os.system("title Nemesis Selfbot v0.2 - Help")
os.system("cls")
print(
    f"""{Fore.MAGENTA}
                                            ╔╗╔╔═╗╔╦╗╔═╗╔═╗╦╔═╗
                                            ║║║║╣ ║║║║╣ ╚═╗║╚═╗
        {Fore.LIGHTMAGENTA_EX}                                    ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═╝
                                    ╔══════════════════════════════════╗
                                    {Fore.WHITE}     This is the Help section!
                                    
                                    {Fore.LIGHTMAGENTA_EX}     Version: {Fore.WHITE}{__version__}
                                    {Fore.LIGHTMAGENTA_EX}     Commands: {Fore.WHITE}{__commands__}{Fore.LIGHTMAGENTA_EX}
                                    ╚══════════════════════════════════╝
""")
print("")
print(Fore.LIGHTMAGENTA_EX+" [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.LIGHTMAGENTA_EX+" Fun Commands.")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Wanted" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To generate a Wanted meme Image")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Meme" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To view a Reddit Meme")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Tweet" + Fore.LIGHTMAGENTA_EX+" <User whithout @>" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To view a generate a Tweet")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" iPhoneX" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To view a generate a iPhone X Image")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" WhoWouldWin" + Fore.LIGHTMAGENTA_EX+" <User 1> <User2>" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To view a generate a Who Would Win Image")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Captcha" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.LIGHTMAGENTA_EX+" <Text>" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To view a generate a Captcha (Meme) Image")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" ChangeMyMind" + Fore.LIGHTMAGENTA_EX+" <Text>" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To view a generate a Change My Mind Image")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Lolice" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.WHITE+" To Lolice someone")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Awooify" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.WHITE+" To Awooify someone")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Blurpify" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.WHITE+" To Blurpify someone pic")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Deepfry" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.WHITE+" To Deepfry someone pic")
print("")
print(Fore.LIGHTMAGENTA_EX+" [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.LIGHTMAGENTA_EX+" Chat Commands.")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Ascii" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To write a text in Ascii")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Embed" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To write a embed text")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" TableFlip" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To write TableFlip Emoji ")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" UnFlip" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To write UnFlip Emoji ")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Shrug" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To write the Shrug Emoji")
print("")
print(Fore.LIGHTMAGENTA_EX+" [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.LIGHTMAGENTA_EX+" Util Commands.")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Ping" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To see your Websocket Ping")
print("")
print(Fore.LIGHTMAGENTA_EX+" [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.LIGHTMAGENTA_EX+" Image Commands.")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Av" + Fore.LIGHTMAGENTA_EX+" <User>" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To see someone's avatar")
print("")
print(Fore.LIGHTMAGENTA_EX+" [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.LIGHTMAGENTA_EX+" Raid Commands.")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" SpamText" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To send a long text that bypasses all anti-raid bots")
print(Fore.LIGHTMAGENTA_EX+"     [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" SpamCrasher" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To send a crasher that bypasses all anti-raid bots (No Anti-Links)")
print("")
print(Fore.LIGHTMAGENTA_EX+" [" + Fore.WHITE+"+" + Fore.LIGHTMAGENTA_EX+"]" + Fore.WHITE+" Menu" + Fore.LIGHTMAGENTA_EX+" |" + Fore.WHITE+" To go to the Main Menu")
print("")
help = input(Fore.LIGHTMAGENTA_EX+" nemesis" + Fore.WHITE+"@" + Fore.LIGHTMAGENTA_EX+"selfbot" + Fore.WHITE+":"+ Fore.CYAN+"~" + Fore.LIGHTMAGENTA_EX+"<3 " + Fore.WHITE+"")
if help == "Menu":
    os.system("cls")
    os.system("main.py")
if help == "menu":
    os.system("cls")
    os.system("main.py")
if help == "MENU":
    os.system("cls")
    os.system("main.py")
if help == "mENU":
    os.system("cls")
    os.system("main.py")