from discord.ext import commands  # Again, we need this imported
import discord

import asyncio
import os
import datetime
from discord.utils import get
import json

from typing import Union

user2 = ""


class ticket3(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context = True, name="ticket3")
    @commands.has_any_role(983975830868860958)
    async def ticket3(self, ctx: commands.Context):
        guild = ctx.guild
        embed = discord.Embed(
            title = 'Demon Ticket system',
            description = 'React with 🎉 to make a Giveaway ticket.',
            color = 0
        )
    
        embed.set_footer(text="ticket system")
    
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("🎉")
    
        while True:
            def check(reaction, user):
                global user2
                user2 = user
                if user != self.bot.user:
                    return str(reaction) == '🎉'
            
            await self.bot.wait_for("reaction_add", check=check)
            #await ctx.send("beidl")
            await msg.remove_reaction("🎉", user2)
            member = user2
            staff = get(guild.roles, id=983975830868860958)

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True),
                staff: discord.PermissionOverwrite(read_messages=True)
            }

            channel = await guild.create_text_channel(f"Giveaway-{member.display_name}", overwrites=overwrites, category=discord.utils.get(ctx.guild.categories, id=984513720820588614))
            embed = discord.Embed(title=f"Giveaway Ticket from {member.display_name}!", description=f"**Congratulations!**\n Please wait patiently a {staff.mention} will be with you shortly!\n \nYou can close this Ticket by running the ***close** command!")
            await channel.send(embed=embed)
            await channel.send(f"{staff.mention}", delete_after=1)
            await channel.send(f"{member.mention}", delete_after=1)

def setup(bot: commands.Bot):
    bot.add_cog(ticket3(bot))
