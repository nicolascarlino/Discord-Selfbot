# coding: utf-8
#!/usr/bin/env python

__version__ = "v1.0"
__setprefix__ = "Set Your Prefix!"
__commands__ = "25"

#<--------------Imports Start & Loading-------------->

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
progressbar = tqdm([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')
import discord
import pyfiglet
import requests
import threading
import re
import traceback
import sys
import base64
import praw
import aiohttp
import time
import random
import json
import shutil
import datetime
import asyncio
from discord.ext import commands
from discord import Color, message
from discord.enums import Status
from PIL import Image
from io import BytesIO
from datetime import *
#<--------------Imports End-------------->

#<--------------Steps Start-------------->

async def step_1():
    print('')
os.system("cls")
os.system("title Nemesis Selfbot v1.0 - Step (1/1)")
print(
    f"""
{Fore.MAGENTA}
                                                ╔╗╔╔═╗╔╦╗╔═╗╔═╗╦╔═╗
                                                ║║║║╣ ║║║║╣ ╚═╗║╚═╗
            {Fore.LIGHTMAGENTA_EX}                                    ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═╝
                                        ╔══════════════════════════════════╗
                                        {Fore.LIGHTMAGENTA_EX}     User ID: {Fore.WHITE}
                                        {Fore.LIGHTMAGENTA_EX}     Prefix: {Fore.WHITE}{__setprefix__}
                                        {Fore.LIGHTMAGENTA_EX}     Version: {Fore.WHITE}{__version__}
                                        {Fore.LIGHTMAGENTA_EX}     Commands: {Fore.WHITE}{__commands__}{Fore.LIGHTMAGENTA_EX}
                                        ╚═══════════════════════════════════╝
    """)

print("")
prefix = input(Fore.MAGENTA+" nemesis" + Fore.WHITE+"@" + Fore.MAGENTA+"selfbot" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+"<3 ")
bot = commands.Bot(description="test", command_prefix={prefix}, self_bot=True)
bot.remove_command('help')

#<--------------Steps End-------------->

#<--------------Logging Start-------------->
os.system("cls")
os.system("title Nemesis Selfbot v1.0 - Logging in...")
from tqdm import tqdm, trange
from time import sleep
print(
    f"""
{Fore.MAGENTA}
                                                ╔╗╔╔═╗╔╦╗╔═╗╔═╗╦╔═╗
                                                ║║║║╣ ║║║║╣ ╚═╗║╚═╗ {Fore.LIGHTMAGENTA_EX}
                                                ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═╝ 

                                                {Fore.WHITE}    Logging in...


""")
print(f"{Fore.MAGENTA}")
progressbar = tqdm([1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')
#<--------------Logging End-------------->

#<--------------Ready Start-------------->
@bot.event
async def on_ready():
    os.system("title Nemesis Selfbot v0.2 - Ready")
    os.system("cls")
    print("")
    print(
        f"""{Fore.MAGENTA}
                                                ╔╗╔╔═╗╔╦╗╔═╗╔═╗╦╔═╗
                                                ║║║║╣ ║║║║╣ ╚═╗║╚═╗ {Fore.LIGHTMAGENTA_EX}
                                                ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═╝
                                        ╔══════════════════════════════════╗
                                        {Fore.LIGHTMAGENTA_EX}     Username: {Fore.WHITE}{bot.user.name}
                                        {Fore.LIGHTMAGENTA_EX}     User ID: {Fore.WHITE}{bot.user.id}
                                        {Fore.LIGHTMAGENTA_EX}     Prefix: {Fore.WHITE}{prefix}
                                        {Fore.LIGHTMAGENTA_EX}     Version: {Fore.WHITE}{__version__}
                                        {Fore.LIGHTMAGENTA_EX}     Commands: {Fore.WHITE}{__commands__}{Fore.LIGHTMAGENTA_EX}
                                        ╚═══════════════════════════════════╝
""")

#<--------------Commands Start-------------->
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        embed = discord.Embed(title="**Command Not Found**", description ="**This command does not exist!**", color = discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
        await ctx.send (embed=embed)


print("")
print("")

# Ascii
@bot.command()
async def ascii(ctx, *, args):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f'```{text}```')


# Embed
@bot.command()
async def embed(ctx, *, text):
    await ctx.message.delete()
    embed = discord.Embed(description = text, color = discord.Color.magenta())
    embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
    await ctx.send (embed=embed)


# Custom Status 

# Playing
@bot.command()
async def playing(ctx, *, args):
    await ctx.message.delete() 
    await bot.change_presence(activity = discord.Game(name=(f"{message}")))

# Streaming
@bot.command()
async def streaming(ctx, *, args):
    await ctx.message.delete() 
    await bot.change_presence(activity = discord.Streaming(name=f"{message}", url="my_twitch_url"))

# Listening
@bot.command()
async def listening(ctx, *, args):
    await ctx.message.delete() 
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name=f"{message}"))

# Watching
@bot.command
async def watching(ctx, *, args):
    await ctx.message.delete() 
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name=f"{message}"))

# SpamText
@bot.command()
async def spamtext(ctx):
    await ctx.message.delete() 
    await ctx.send(f"0̤龘̈︶（龘龘龘龘8龘_̤*龘龘&-╭╭21龘龘龘龘龘龘̈龘☣̈~3̤∩龘̈╭̤龘龘龘龘!♀̈龘̈╮8⇝̈9龘d8龘龘̈!龘╮龘龘︿9̈龘꧂龘龘龘龘龘w︶龘龘龘龘龘̈!龘5406龘⇝∩龘龘（龘︶龘8龘$9@-龘̈╮龘龘龘!̈龘2龘♀龘-$龘∩8╮龘4╮龘龘龘龘6̈龘龘̤w龘*̈∩龘龘龘龘龘龘̈龘27ヅ#龘（龘5龘∩%w龘╮龘龘龘龘龘龘龘龘龘̈龘龘1龘龘龘龘∩龘龘龘:龘龘龘⇝̤︶龘̤22龘d龘龘龘_龘:꧂龘龘龘︶龘╮龘龘龘（龘龘龘︿龘3龘龘龘龘☠龘2︶龘@龘ヅ龘龘龘龘̈龘d龘龘龘龘龘龘龘龘#*龘9~6龘̤☠~龘龘龘龘龘龘龘龘龘龘8龘̈8龘龘龘➤龘5龘龘̈⇝龘&➤2:$龘龘龘̈d龘龘（︶龘~_⇝~龘龘龘d@⇝d龘̤⇝∩ヅ龘̤龘╮）龘꧂̈龘龘1龘龘☣9╮龘龘龘龘龘（龘╭:龘龘꧂龘（~∩8♀@̈龘1龘̈龘龘♀0龘龘龘龘@$龘w☣龘龘꧂龘̤龘龘龘龘龘龘龘龘龘̤%龘龘龘）龘龘龘8龘龘龘龘5#龘龘龘3w龘龘龘☣77龘龘*龘龘龘龘̤龘̤龘龘4龘0龘*&龘̤龘龘龘@龘龘龘龘龘╭%w龘☠4龘龘w!龘龘龘︶龘8龘龘︶w龘龘̤龘龘龘龘76龘龘_̤龘̈꧂8龘龘龘☣̈龘6龘龘龘̤$35~︶#➤龘龘龘#龘☠龘̤龘）龘☠0龘:龘龘龘龘@$龘︶龘龘龘︿龘2龘龘龘꧁）龘龘☣龘龘̈龘1*龘➤̤龘龘龘3^-龘08龘̤~&╭龘龘̈龘龘龘2龘!龘龘5龘︶龘#龘龘龘龘龘龘☣龘龘̤-♀☣@~^龘龘̈龘龘∩龘d̤︶w龘╮!╭︶龘龘龘龘龘龘龘!̈d（꧂龘龘w龘龘龘̤⇝龘龘龘̈龘57*d龘龘̤&龘龘╮$︶龘0龘（̤%龘龘龘龘龘̤龘龘龘6̈龘̈龘@龘龘龘龘龘龘龘9龘28龘龘2̤∩龘꧁w̤龘ヅ̈꧁4龘龘龘~̤龘龘龘ヅ龘̈︿龘龘w!龘@龘龘龘☠龘︿龘龘龘2#ヅ︶&︶龘$龘$龘☠@_☣︿2龘龘龘龘0︶☠8龘w龘:꧁w︿龘（龘̤0龘♀龘1:龘龘龘龘龘龘╭龘龘）龘龘龘2龘龘꧂̈龘$龘龘龘龘龘龘︶龘︶̈龘龘龘:̈︶龘♀∩龘ヅ龘龘3龘龘̈龘龘7w龘2龘龘4➤龘*龘︿̈龘╮龘龘龘龘龘̈∩28♀龘%龘龘!龘︶龘&꧁龘龘龘5龘:!龘5龘̤龘龘☣̈龘龘龘➤_龘:龘龘龘龘7龘龘➤:龘╭:（龘龘龘龘꧁）龘龘龘龘_꧁龘∩̈➤̈꧂龘:龘9*!#∩龘龘龘➤龘̈龘龘龘龘龘%龘龘@̤∩龘龘╭）➤龘龘龘龘∩龘龘龘龘龘龘龘龘龘#꧂（龘龘龘龘龘̈⇝☠%︶⇝龘♀:龘龘:♀龘♀龘^龘꧁3⇝龘:17⇝☣4龘1龘龘龘2龘龘︶$龘龘龘̤d龘2̤龘∩1̤龘7龘龘☣̤龘꧂8#龘龘龘）☠︶龘⇝꧂龘龘19龘*龘龘龘龘龘龘龘2♀̤龘73龘$066̈龘~龘9龘龘龘̤4龘龘龘龘龘̤龘龘#☣̤龘龘龘:龘龘☠龘̈@:龘龘龘➤7龘̤6（2~龘龘:龘龘（龘꧂꧁龘龘龘龘龘̤̈^龘w龘龘龘6➤龘（龘︿龘̤6龘̈龘5♀龘5☣龘9-龘龘龘╭龘龘龘龘∩☣龘9!0̈♀꧂_龘∩龘龘龘龘╭）龘$龘!龘̤龘龘5龘龘︿龘龘龘4$龘2╭̈5龘龘龘7*龘龘5龘龘龘:*龘龘_龘龘꧁︶龘龘龘龘龘龘龘龘龘2龘龘龘d︿龘╮̤꧁4╮龘龘龘︿1龘8~龘4龘459龘龘龘:꧁$龘̈龘70龘龘ヅ4龘∩꧁-1龘꧁_龘龘☠龘龘龘龘∩龘龘）龘龘̈80龘龘龘龘龘︿龘龘龘57龘☠龘3$龘龘∩龘龘龘⇝龘龘龘4龘̤龘5̈⇝꧁∩龘︿∩龘꧂&︶龘龘龘➤2@龘ヅ龘☠#̈3︶╭龘*龘╭龘龘$0龘龘3龘龘龘（23龘龘龘龘0龘龘龘龘&龘龘︶龘ヅ龘➤:!龘龘-龘龘龘3龘龘龘̤̤龘꧂9龘̈龘龘龘龘龘:︿:☠♀╭龘龘龘∩̤ヅ67╮龘╮_龘龘龘︶꧂龘╮龘♀龘龘̈龘w:龘龘龘d☠☠龘龘&龘8龘︶_1龘龘*w0龘ヅ17龘龘龘5龘2#龘6龘7龘d̤2龘➤龘龘̈*龘龘︶⇝☣ヅ╭꧁̤龘龘龘龘龘╮龘龘@%龘̤龘龘@龘*⇝%龘龘龘龘龘龘龘0w龘龘龘龘̈龘5∩龘龘龘龘︶龘龘̤龘龘龘:-龘9龘#龘龘龘^龘龘5╮&龘龘︶龘1➤龘龘龘龘龘̤$♀^&!$龘龘_^龘龘龘龘6☠$龘龘龘̈&龘-@龘龘龘龘̤4龘（龘龘̈龘龘龘龘&龘龘龘7龘☣̈&☠龘龘龘*2龘龘龘5龘̈_龘龘!龘龘33龘龘^%龘（龘-0@龘☠:龘龘龘̤龘$龘龘龘龘龘꧂）龘龘&龘^龘♀︿龘龘龘龘龘龘☣龘龘龘̤╭5龘（!龘^̈）w龘3➤龘龘︿龘2̤龘龘423龘*龘龘☠̤龘╭龘龘龘∩（龘6龘0龘龘龘龘龘∩龘-龘︿龘~龘龘꧁2龘̤龘龘⇝~龘龘龘♀龘龘︶1̤龘龘龘1&8̈︶龘꧂龘龘7@_龘龘龘☠龘~#龘龘龘龘̈5︿龘龘龘龘龘龘龘龘龘8龘⇝54龘龘）龘̤̤（3ヅ4︿︿龘龘*龘꧁龘:1╮龘龘♀*︶龘龘龘龘︿:48:∩^32龘1龘:龘*龘龘龘龘☠龘╭龘4龘4龘!龘5龘︶#龘龘龘╭龘꧂龘）ヅ龘龘龘龘936龘̤龘꧂龘龘5龘0︶︶龘4︿龘龘龘̤龘!︶☣_龘龘龘龘龘&4龘龘龘59龘龘6龘龘龘♀╭̈龘⇝╮龘龘龘╮:-龘龘︶⇝_̈龘&̤̤龘̤̤8龘♀╮~龘龘#̤8龘龘龘龘龘龘龘̈龘龘龘龘（龘d龘龘龘龘꧂龘︶2龘#（龘:龘龘:6:龘:̤龘龘7̈̈龘⇝龘龘̈龘龘龘̤龘9龘_∩龘龘@龘╮@龘龘6#龘-龘̤0*龘龘*龘龘~♀")

# SpamCrasher
@bot.command()
async def spamcrasher(ctx):
    await ctx.message.delete()
    await ctx.send(f"https://tenor.com/view/minecraft-reddit-funny-gif-14138658?size=我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地将你的悲惨的屁股子。我将尽其所能地")


# Cls
@bot.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system("cls")
    print("")
    print(
        f"""{Fore.MAGENTA}
                                                ╔╗╔╔═╗╔╦╗╔═╗╔═╗╦╔═╗
                                                ║║║║╣ ║║║║╣ ╚═╗║╚═╗ {Fore.LIGHTMAGENTA_EX}
                                                ╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═╝
                                        ╔══════════════════════════════════╗
                                        {Fore.LIGHTMAGENTA_EX}     Username: {Fore.WHITE}{bot.user.name}
                                        {Fore.LIGHTMAGENTA_EX}     User ID: {Fore.WHITE}{bot.user.id}
                                        {Fore.LIGHTMAGENTA_EX}     Prefix: {Fore.WHITE}{prefix}
                                        {Fore.LIGHTMAGENTA_EX}     Version: {Fore.WHITE}{__version__}
                                        {Fore.LIGHTMAGENTA_EX}     Commands: {Fore.WHITE}{__commands__}{Fore.LIGHTMAGENTA_EX}
                                        ╚═══════════════════════════════════╝
""")


# TableFlip
@bot.command()
async def tableflip(ctx):
    await ctx.message.delete()
    await ctx.send("""(╯°□°）╯︵ ┻━┻""")

# UnFlip
@bot.command()
async def unflip(ctx):
    await ctx.message.delete()
    await ctx.send("""┬─┬ ノ( ゜-゜ノ)""")

# Shrug
@bot.command()
async def shrug(ctx):
    await ctx.message.delete()
    await ctx.send("¯\_(ツ)_/¯")


# V0.2


# Ping
@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title = "**Pong!**", color = discord.Color.magenta(), description = f"**{round(bot.latency * 1000)}ms**")
    embed.set_footer(text="Nemesis Selfbot")
    icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg'
    await ctx.send(embed=embed)

# Avatar
@bot.command()
async def av(ctx, user: discord.User=None):
    if user is None:
        user = ctx.author
        url = user.avatar_url
        await ctx.message.delete()
        embed = discord.Embed(color=discord.Color.magenta(), title=f"{user}")
        embed.set_image(url=f"{url}")
        embed.set_footer(text="Nemesis Selfbot")
        icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg'
        await ctx.send(embed=embed)


# Meme
reddit = praw.Reddit(client_id = "",
                     client_secret = "",
                     username = "", 
                     user_agent = "pythonpraw")
@bot.command()
async def meme(ctx):
    await ctx.message.delete()
    subreddit = reddit.subreddit('meme')
    all_subs = []
    top = subreddit.top(limit = 50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    embed = discord.Embed(title = name)
    embed.set_image(url = url)
    embed.set_footer(text="Nemesis Selfbot")
    icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg'
    await ctx.send(embed=embed)

# Wanted
@bot.command()
async def wanted(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    wanted = Image.open("wanted.jpg")
    asset = user.avatar_url_as(size = 512)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((322, 324))
    wanted.paste(pfp, (123, 254))
    wanted.save("profile.jpg")
    await ctx.send(file = discord.File("profile.jpg"))

# Help
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    os.system("cls")
    os.system("help.py")
    embed = discord.Embed(color = discord.Color.magenta(), description = "**Help Window already Opened!**")
    embed.set_footer(text="Nemesis Selfbot")
    await ctx.send(embed=embed)

# Tweet
@bot.command()
async def tweet(ctx, username:str=None, *, message:str=None):
    await ctx.message.delete()
    if username is None:
        embed = discord.Embed(description="**You neeed to specify the username in the tweet!**", color=discord.Color.dark_red())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# iPhoneX
@bot.command()
async def iphonex(ctx, user: discord.User=None, *, message:str=None):
    await ctx.message.delete()
    if user is None:
        embed = discord.Embed(description="**You neeed to specify the username!**", color=discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        async with aiohttp.ClientSession() as cs:
            url = user.avatar_url
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={url}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# WhoWouldWin
@bot.command()
async def whowouldwin(ctx, user: discord.User=None, *, message:str=None):
    await ctx.message.delete()
    if user is None:
        embed = discord.Embed(description="**You neeed to specify the usernames!**", color=discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        async with aiohttp.ClientSession() as cs:
            url1 = user.avatar_url
            url2 = user.avatar_url
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={url1}&user2={url2}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# Captcha
@bot.command()
async def captcha(ctx, user: discord.User=None, *, message:str=None):
    await ctx.message.delete()
    if user is None:
        embed = discord.Embed(description="**You neeed to specify the username!**", color=discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        async with aiohttp.ClientSession() as cs:
            url = user.avatar_url
            username = user.name
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={url}&username={username}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# ChangeMyMind
@bot.command()
async def changemymind(ctx, *, message:str=None):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        user = ctx.author
        if user is None:
            embed = discord.Embed(description="**You neeed to specify the username!**", color=discord.Color.magenta())
            embed.set_footer(text="Nemesis Selfbot")
            await ctx.send(embed=embed)
        else:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={message}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# Lolice
@bot.command()
async def lolice(ctx, user: discord.User=None):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        url = user.avatar_url
        user = ctx.author
        if user is None:
            embed = discord.Embed(description="**You neeed to specify the username!**", color=discord.Color.magenta())
            embed.set_footer(text="Nemesis Selfbot")
            await ctx.send(embed=embed)
        else:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=lolice&url={url}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# Awooify
@bot.command()
async def awooify(ctx, user: discord.User=None, *, message:str=None):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        url = user.avatar_url
        user = ctx.author
        if user is None:
            embed = discord.Embed(description="**You neeed to specify the username!**", color=discord.Color.magenta())
            embed.set_footer(text="Nemesis Selfbot")
            await ctx.send(embed=embed)
        else:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={url}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# Deepfry
@bot.command()
async def deepfry(ctx, user: discord.User=None, *, message:str=None):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        image = user.avatar_url
        user = ctx.author
    if user is None:
        embed = discord.Embed(description="**You neeed to specify the username!**", color=discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        async with aiohttp.ClientSession() as cs:
            url = user.avatar_url
            user = ctx.author
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=deepfry&image={image}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# Blurpify
@bot.command()
async def blurpify(ctx, user: discord.User=None, *, message:str=None):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        image = user.avatar_url
        user = ctx.author
    if user is None:
        embed = discord.Embed(description="**You neeed to specify the username!**", color=discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        async with aiohttp.ClientSession() as cs:
            url = user.avatar_url
            user = ctx.author
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=blurpify&image={image}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)


# v0.3

# TrumpTweet
@bot.command()
async def trumptweet(ctx, *, message:str=None):
    await ctx.message.delete()
    if message is None:
        embed = discord.Embed(description="**You neeed to specify the text in the tweet!**", color=discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={message}") as r:
                data = await r.json()
                embed = discord.Embed(description="**Done!**", color=discord.Color.magenta())
                embed.set_image(url=data["message"])
                embed.set_footer(text="Nemesis Selfbot", icon_url='https://image.freepik.com/vector-gratis/angry-and-cruel-panda-gaming-esport-mascot-logo_221276-7.jpg')
                await ctx.send(embed=embed)

# BypassImg
@bot.command()
async def bypassimg(ctx, *, message:str=None):
    await ctx.message.delete()
    if message is None:
        embed = discord.Embed(description="**You neeed to specify the Image!**", color=discord.Color.magenta())
        embed.set_footer(text="Nemesis Selfbot")
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"{message}")

# Eyesrape
@bot.command()
async def eyesrape(ctx):
    await ctx.message.delete()
    await ctx.send(f"https://tenor.com/view/warning-scammer-gif-10826981")

# Wait, Are you a femboy?
@bot.command()
async def areyoufemboy(ctx):
    await ctx.message.delete()
    await ctx.send(f"https://tenor.com/view/wait-cat-are-you-afemboy-cute-femboy-gif-17221762")



#<--------------Commands End-------------->
#<--------------Ready End-------------->



#<-------------- Get Token Start ------------------>
with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
bot.run(token, bot=False)
#<-------------- Get Token End ------------------>