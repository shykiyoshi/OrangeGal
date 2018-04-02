from decimal import Decimal
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "r!")

chat_filter = ["RIN"]
bypass_list = []

@client.event
async def on_ready():
    print("I'm ready, Kiyo~! ^o^")
    await client.change_presence(game=discord.Game(name='with Lenny~'))

@client.event
async def on_message(message):
    # hi command
    if message.content == "r!hi":
        userID = message.author.id
        await client.send_message(message.channel, "Hi, <@%s>~ :wave:" % (userID))
    # lewd command
    if message.content == "r!lewd":
        await client.send_message(message.channel, "Who lewded me? ಠ▃ಠ Hmph. Rood!")
    # rin mentioned
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                await client.send_message(message.channel, "Did someone mention my name?? OwO")
    # omg lolz
    if message.content == "r!omg":
        await client.send_file(message.channel,"omg.png")
    # kiyo time
    if message.content == "r!kiyotime":
        userID = message.author.id
        import datetime
        currentDT = datetime.datetime.now()
        x = Decimal((currentDT.minute / 60 + currentDT.hour) * 5.0/12)
        kiyotime = round(Decimal(x),4)
        await client.send_message(message.channel,(":alarm_clock: <@%s>, The current time is..." % (userID)))
        await client.send_message(message.channel,(kiyotime))
    # orange
    if message.content.startswith('r!orange'):
        targetID = message.content[9:]
        await client.send_message(message.channel,("%s, you got an orange! Stay healthy, fellow yellow! :tangerine:" % (targetID)))
    # admirer
    if message.content.startswith('r!love'):
        targetID = message.content[7:]
        await client.delete_message(message)
        await client.send_message(message.channel,("%s, someone just told me that they love you! :eyes: Not telling who though~" % (targetID)))

client.run(process.env.BOT_TOKEN)
