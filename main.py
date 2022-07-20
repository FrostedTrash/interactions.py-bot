import discord

from datetime import datetime
import threading

import requests

import os

import interactions
from interactions.ext.get import get

import time

intents = discord.Intents.default()
intents.members = True

bot = interactions.Client(token="token", intents=interactions.Intents.ALL)


import threading

#bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot Online!")
    await bot.change_presence(interactions.ClientPresence(activities=[interactions.PresenceActivity(name="Moon Development™", type=interactions.PresenceActivityType.WATCHING)]))
    r = requests.head(url="https://discord.com/api/v1")
    try:
      print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
    except:
      print("No rate limit")

def checkTime():

    threading.Timer(1, checkTime).start()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print(current_time)
    if(current_time == '23:00:00'): 
        f = open('gen.txt', 'r+')
        f.truncate(0)
        f.close()


@bot.command(
    name="coglist",
    description="Shows a list of all Scripts"
)
async def coglist(ctx):
    f = open("cogs.txt","r+")
    f.truncate(0)
    f.close()
    for filename in os.listdir('./'):
        if filename.endswith('.py'):
            f2 = open("cogs.txt", "r+")
            f2.seek(0, os.SEEK_END)
            f2.writelines(f"{filename[0:-3]}")
            f2.writelines("\n")
            f2.close()
    f = open("cogs.txt")
    lines = f.read()
    f.close()
    await ctx.send(f"{lines}")

@bot.command(
    name="reload",
    description="reload a cog",
    options = [
        interactions.Option(
            name="cog",
            description="The cog you want to reload",
            type=interactions.OptionType.STRING,
            required=True,
        )
    ]
)
async def reload(ctx: interactions.CommandContext, cog: str):
    if 997250141985710207 not in ctx.author.roles:
        embed = interactions.Embed(title="No Permission", description=f"You do not have the required Role!", color=0xE74C3C)
        await ctx.send(embeds=embed)
    
    try:
        bot.reload(f"{cog}")
        msg = await ctx.send(f"Cog **{cog}** reloaded!")
    except:
        msg = await ctx.send(f"Couldn't reload **{cog}**!")
    time.sleep(1)
    await msg.delete()

#send.start()
#bot.load("key")

bot.load("auth")
bot.load("ticket")

#keep_alive()


bot.start()
