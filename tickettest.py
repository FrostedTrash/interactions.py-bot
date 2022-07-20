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

    @commands.command(pass_context = True, name="tickettest")
    @commands.has_any_role(922247919711711263)
    async def tickettest(self, ctx: commands.Context):
        guild = ctx.guild
        embed = discord.Embed(
            title = 'Demon Ticket system',
            description = 'React with 💸 to make a Buy ticket.',
            color = 0
        )
    
        embed.set_footer(text="ticket system")
    
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("💸")
    
        while True:
            def check(reaction, user):
                global user2
                user2 = user
                if user != self.bot.user:
                    return str(reaction) == '💸'
            
            await self.bot.wait_for("reaction_add", check=check)
            #await ctx.send("beidl")
            await msg.remove_reaction("💸", user2)
            member = user2
            staff = get(guild.roles, id=922247919711711263)

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True),
                staff: discord.PermissionOverwrite(read_messages=True)
            }

            channel = await guild.create_text_channel(f"Buy-{member.display_name}", overwrites=overwrites, category=discord.utils.get(ctx.guild.categories, id=921350024867242024))
            embed = discord.Embed(title=f"Buy Ticket from {member.display_name}!", description=f"Hello!\n Please wait patiently a {staff.mention} will be with you shortly!\nIn the meantime you can already describe what you are going to buy.\n \nYou can close this Ticket by running the ***close** command!")
            Id = user2.id
            channelid = channel.id
            y = {"channel":channelid, "user":Id}
            with open ("users.json", "r+") as file:
                file_data=json.load(file)
                file_data["users"].append(y)
                file.seek(0)
                json.dump(file_data,file,indent=4)
            await channel.send(embed=embed)
            await channel.send(f"{staff.mention}", delete_after=1)
            await channel.send(f"{member.mention}", delete_after=1)


    @commands.command(pass_context = True)
    async def close1(self, ctx: commands.Context):
        author = ctx.author
        guild = ctx.guild
        owner = get(guild.roles, id=922247919711711263)
        everyone_role = guild.roles[0]

        if ctx.channel.category is not None:
            if ctx.channel.category.id == 921350024867242024:
                #await ctx.channel.edit(category=discord.utils.get(ctx.guild.categories, id=929372434027647016))
                with open("users.json", "r") as f:
                    data = json.load(f)
                    for person in data['users']:
                        if ctx.channel.id == person["channel"]:
                            userid = person["user"]
                            user = ctx.guild.get_member(userid)
                            print(userid)
                            print(user)
                embed = discord.Embed(title="Closed", description=f"Ticket has been closed by {ctx.author}.", colour=0xE74C3C)
                await ctx.send(embed=embed)

                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = False
                overwrite.read_messages = False
                                
                
                await ctx.channel.set_permissions(user, overwrite=overwrite)
                #await ctx.channel.set_permissions(owner, read_messages=True)
                await ctx.message.delete()

def setup(bot: commands.Bot):
    bot.add_cog(ticket(bot))
