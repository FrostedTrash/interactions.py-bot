from discord.ext import commands # Again, we need this imported
import discord


class Embeds(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

"""Empty embed"""
#embed = discord.Embed()

"""Embed with Title"""
#embed = discord.Embed(title="Hello, World!")

"""Embed with Title and Text"""
#embed = discord.Embed(title="Hello, World!", description=":D")

"""Embed with Title, Text and Colour"""
#embed = discord.Embed(title="Hello, World!", description=":D", colour=0x87CEEB)

"""Embed with Title, Text, Colour, Author and Icon"""
#embed = discord.Embed(title="Hello, World!", description=":D", colour=0x87CEEB)
#embed.set_author(name="Trashy", icon_url="https://avatars.githubusercontent.com/u/16879430")

"""Embed with Title etc. and 3 Fields"""
#embed = discord.Embed(title="Hello, world!", description=":D", colour=0x87CEEB)
#embed.set_author(name="vcokltfre", icon_url="https://avatars.githubusercontent.com/u/16879430")
#embed.add_field(name="Field 1", value="Not an inline field!", inline=False)
#embed.add_field(name="Field 2", value="An inline field!", inline=True)
#embed.add_field(name="Field 3", value="Look I'm inline with field 2!", inline=True)

"""Embed with Title etc, Fields and Footer with date!"""
#from datetime import datetime

#embed = discord.Embed(title="Hello, world!", description=":D", colour=0x87CEEB, timestamp=datetime.utcnow())
#embed.set_author(name="vcokltfre", icon_url="https://avatars.githubusercontent.com/u/16879430")
#embed.add_field(name="Field 1", value="Not an inline field!", inline=False)
#embed.add_field(name="Field 2", value="An inline field!", inline=True)
#embed.add_field(name="Field 3", value="Look I'm inline with field 2!", inline=True)
#embed.set_footer(text="Wow! A footer!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")

"""Embed with image"""
#e = discord.Embed()
#e.set_image(url="https://discordapp.com/assets/e4923594e694a21542a489471ecffa50.svg")

def setup(bot: commands.Bot):
    bot.add_cog(Embeds(bot))