from discord.ext import commands  # Again, we need this imported
import discord

import asyncio
import os
import datetime
from discord.utils import get
import json

from typing import Union

user2 = ""


class ticket(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context = True, name="sex")
    @commands.has_any_role(983975830868860958)
    async def ticket(self, ctx: commands.Context):
        guild = ctx.guild
        embed = discord.Embed(
            title = 'Ticket system',
            description = 'React 📩 to make a ticket.',
            color = 0
        )
    
        embed.set_footer(text="ticket system")
    
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("📩")
    
        while True:
            def check(reaction, user):
                global user2
                user2 = user
                if user != self.bot.user:
                    return str(reaction) == '📩'
            
            await self.bot.wait_for("reaction_add", check=check)
            #await ctx.send("beidl")
            await msg.remove_reaction("📩", user2)
            member = user2
            staff = get(guild.roles, id=983975830868860958)

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True),
                staff: discord.PermissionOverwrite(read_messages=True)
            }

            channel = await guild.create_text_channel(f"Ticket - {member.display_name}", overwrites=overwrites, category=discord.utils.get(ctx.guild.categories, id=984513720820588614))
            embed = discord.Embed(title=f"Ticket from {member.display_name}!", description=f"Hello!\n Please wait patiently a {staff.mention} will be with you shortly!\nIn the meantime you can already describe what you are going to buy.")
            await channel.send(embed=embed)
            await channel.send(f"{staff.mention}", delete_after=1)
            await channel.send(f"{member.mention}", delete_after=1)


    @commands.command(pass_context = True)
    async def close(self, ctx: commands.Context):
        author = ctx.author
        guild = ctx.guild
        owner = get(guild.roles, id=983975830868860958)

        if ctx.channel.category is not None:
            if ctx.channel.category.id == 984513720820588614:
                #await ctx.channel.edit(category=discord.utils.get(ctx.guild.categories, id=929372434027647016))
                embed = discord.Embed(title="Closed", description=f"Ticket has been closed by {ctx.author}.", colour=0xE74C3C)
                await ctx.send(embed=embed)

                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = False
                overwrite.read_messages = True
                await ctx.channel.set_permissions(author, overwrite=overwrite)
                await ctx.message.delete()

def setup(bot: commands.Bot):
    bot.add_cog(ticket(bot))
