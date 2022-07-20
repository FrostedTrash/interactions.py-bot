from base64 import standard_b64decode
from discord.ext import commands  # Again, we need this imported
import discord

import asyncio
import os
import datetime
import time

import interactions
from interactions.ext.get import get

global guild_id
global staff_role
global owner_role

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263

class getacc(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
      name="account",
      description="Get an Account you defined",
      options = [
            interactions.Option(
                name="game",
                description="Game you need the Account for",
                type=interactions.OptionType.STRING,
                required=True,
                choices=[
                  interactions.Choice(
                    name="FiveM",
                    value="fivem"
                  ),
                  interactions.Choice(
                    name="GTA downloadable",
                    value="gta"
                  ),
                  interactions.Choice(
                    name="Red Dead Redemption 2",
                    value="rdr"
                  ),
                ],
            ),
            interactions.Option(
                name="amount",
                description="Amount of Accounts you need",
                type=interactions.OptionType.INTEGER,
                required=False
            ),
        ],
    )
    async def FiveM(self, ctx: interactions.CommandContext, game: str, amount = 0):
      if staff_role in ctx.author.roles:
        if game == "fivem":
          filename = "accounts.txt"
          gamename = "Fivem"
        elif game == "gta":
          filename = "gtaaccounts.txt"
          gamename = "GTA"
        elif game == "rdr":
          filename = "reddead.txt"
          gamename = "RDR2"
        if staff_role not in ctx.author.roles:
          print("no perms lol")
        if amount == 0:
          f = open(filename, "r")
          count = len(open(filename).readlines())
          print(count)
          f.close()
          if count == 0:
            await ctx.send ("No more accounts!")
            return
          f = open(filename)
          firstline = f.readline()
          f.close()
          now = datetime.datetime.now()
          now2 = now.strftime("%Y-%m-%d, %H:%M:%S")
          
          f3 = open("logs.txt", "r+")
          f3.seek(0, os.SEEK_END)
          f3.writelines(f"{gamename} get: {ctx.author.name}, {now2}")
          f3.writelines("\n")
          f3.close()
          embed = interactions.Embed(title="Your Account",
                            description=f"||{firstline}||",
                            color=0xE67E22)
          embed.set_author(name=f"Command run by {ctx.author.name}",
                       )
          f = open(filename, "r+")
          f4 = open("backup.txt", "r+")
          f4.seek(0, os.SEEK_END)
          f4.writelines(f"{gamename}-- {firstline}")
          f4.close
          lines = f.readlines()
          #Move to first line
          f.seek(0)
          #truncate
          f.truncate()
          #Start writing skipping line 1
          f.writelines(lines[1:])
          f.close()
          f = open(filename)
          count2 = len(open(filename).readlines())
          print(count2)
          f.close()
          embed.set_footer(text=f"{count2} accounts left!")
          await ctx.send(embeds=embed)
          time.sleep(1)
          return
        else:
          amount = int(amount)
          #await ctx.send ("int")
          member = ctx.author
          for x in range(0, amount):
            f = open(filename, "r")
            count = len(open(filename).readlines())
            print(count)
            f.close()
            if count == 0:
                await ctx.send ("No more accounts!")
                break
            f = open(filename) 
            firstline = f.readline()
            f.close()
            now = datetime.datetime.now()
            now2 = now.strftime("%Y-%m-%d, %H:%M:%S")
            f3 = open("logs.txt", "r+")
            f3.seek(0, os.SEEK_END)
            f3.writelines(f"{gamename} get: {ctx.author.name}, {now2}")
            f3.writelines("\n")
            f3.close()
            embed = interactions.Embed(title="Your Account",
                              description=f"||{firstline}||",
                              color=0xE67E22)
            embed.set_author(name=f"Command run by {ctx.author.name}",
                         )
            f = open(filename, "r+")
            lines = f.readlines()
            #Move to first line
            f.seek(0)
            #truncate
            f.truncate()
            #Start writing skipping line 1
            f.writelines(lines[1:])
            f.close()
            f4 = open("backup.txt", "r+")
            f4.seek(0, os.SEEK_END)
            f4.writelines(f"{gamename}-- {firstline}")
            f4.close
            f = open(filename)
            count2 = len(open(filename).readlines())
            print(count2)
            f.close()
            embed.set_footer(text=f"{count2} Accounts left!")
            await ctx.send(embeds=embed)
      else:
        staff = await get(self.bot, interactions.Role, guild_id=guild_id, role_id=staff_role)
        embed = interactions.Embed(title="No Permission", description=f"You do not have the required {staff.mention} Role!", color=0xE74C3C)
        await ctx.send(embeds=embed)

def setup(client):
    getacc(client)
