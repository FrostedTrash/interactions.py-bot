from turtle import color, title
import requests
import json
import discord
from discord.ext import commands
import os

import interactions
from interactions.ext.get import get

api_key = "cd26927a9eba9a816b5a984eeb8abbcf82a4f6d1"

global guild_id
global staff_role
global owner_role

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263

class tipeee_payment(interactions.Extension):
    """A couple of simple commands."""
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
      name="tpc",
      description="Show the last Tipeeestream donation",
      options = [
        interactions.Option(
          name="count",
          description="Use this incase you want to see older donations!",
          type=interactions.OptionType.NUMBER,
          required=False,
          ),
      ],
    )
    async def tpc(self, ctx: interactions.CommandContext, count = 0):
      count = int(count)
      if staff_role in ctx.author.roles:
        def writeJson5(data, filename="auth.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        cd = requests.get(f"https://api.tipeeestream.com/v1.0/events.json?apiKey={api_key}&type[]=donation&type[]=subscription")
        cd.json()
        data = cd.json()
        writeJson5(data)
        try:
            with open ("auth.json", "r") as f4:
                data = json.load(f4)
                datas = data["datas"]
                items = datas["items"]
                i = items[count]
                params = i["parameters"]
                amount = params["amount"]
                if params["fees"] == "":
                    fees = "No"
                elif params["fees"] == 1:
                    fees = "Yes"
                if "message" in i["parameters"]:
                  message = params["message"]
                else: 
                  message = "no message given!"
                username = params["username"]

                print(f"{username}\n{message}\n{amount}€\n{fees}")

                embed = interactions.Embed(title=f"Tipeeestream donation Nr.{count + 1}", color=0x4B0082)
                embed.add_field(name="**Username**", value=f"```{username}```", inline= False)
                embed.add_field(name="**Message**", value=f"```{message}```", inline= False)
                embed.add_field(name="**Amount**", value=f"```{amount}€```", inline= False)
                embed.add_field(name="**Fees paid?**", value=f"```{fees}```", inline= False)

                await ctx.send(embeds=embed)
        except Exception as e:
            print(e)
      else:
        staff = await get(self.bot, interactions.Role, guild_id=guild_id, role_id=staff_role)
        embed = interactions.Embed(title="No Permission", description=f"You do not have the required {staff.mention} Role!", color=0xE74C3C)
        await ctx.send(embeds=embed)

def setup(client):
    tipeee_payment(client)
