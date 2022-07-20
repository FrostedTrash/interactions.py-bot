from discord.ext import commands  # Again, we need this imported
import discord

import interactions
from interactions.ext.get import get

import time

global guild_id
global staff_role
global owner_role

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263

class embedmaker(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="embedmaker",
        description="Make any embed!",
        options = [
            interactions.Option(
                name="title",
                description="Title of the Embed",
                type=interactions.OptionType.STRING,
                required=True
            ),
            interactions.Option(
                name="text",
                description="The text of the Embed",
                type=interactions.OptionType.STRING,
                required=False
            ),
            interactions.Option(
                name="color",
                description="Set the color of the Embed",
                type=interactions.OptionType.STRING,
                required=False,
                choices=[
                    interactions.Choice(
                        name="Red",
                        value="red",
                    ),
                    interactions.Choice(
                        name="Blue",
                        value="blue",
                    ),
                    interactions.Choice(
                        name="Green",
                        value="green",
                    ),
                ],
            ),
            interactions.Option(
                name="channel",
                description="Channel ID to send the Embed to",
                type=interactions.OptionType.STRING,
                required=False,
            ),
        ],
    )
    async def embedmaker(self, ctx: interactions.CommandContext,title: str,channel = 0, text = "", color = 0x7289DA):
        if staff_role in ctx.author.roles:
            if color == "red":
                color = 0xE74C3C
            elif color == "blue":
                color = 0x7289DA
            elif color == "green":
                color = 0x2E8B57
            else:
                color = 0x7289DA
            embed = interactions.Embed(title=title, description=text, colour=color)
            guild = await ctx.get_guild()
            if channel != 0:
                channel = await get(self.bot, interactions.Channel, channel_id=channel)
                await ctx.send("Embed sent to channel")
                time.sleep(3)
                await ctx.message.delete()
            else:
                channel =  await ctx.get_channel()
            await channel.send(embeds=embed)


def setup(client):
    embedmaker(client)
