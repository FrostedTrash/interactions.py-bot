from discord.ext import commands  # Again, we need this imported
import discord

import asyncio
import os
from datetime import datetime, timedelta
from discord.utils import get
import json
import discord


class Vorlage(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    #bans a user with a reason
    @commands.command(pass_context=True, aliases=["pp"])
    async def paypal (self, ctx:commands.Context):
        await ctx.message.delete(delay=1)
        await ctx.send(f"trashypaypal@gmail.com \n**if you dont pay with __F&F__ you dont get your product**")
        
    @commands.command(name = "tipeee")
    async def tipeee (self, ctx: commands.Context, member:discord.User=None):
        embed = discord.Embed(title="Tipeeestream Payment", description=f" ", color=0x800000)
        embed.add_field(name="Link", value="Please pay here:\nhttps://www.tipeeestream.com/trashy-mc/donation/", inline=False)
        embed.add_field(name="Fees", value="Make sure you make the **Tick** as shown in the picture below!\n If you don't do this you will **NOT** get your product or refund!\n **pls write you discord name in the message!**", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/942404842645762088/942496963914498148/Screenshot_130.png"
        )
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_any_role(983975830868860958)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)
        await ctx.send(f'Cleared by {ctx.author.mention}', delete_after = 10)

    @commands.command(pass_context=True)
    @commands.has_any_role(983975830868860958)
    async def ban (self, ctx, member:discord.User=None, reason =None):
        author = ctx.author
        if member == None or member == author:
            await ctx.channel.send("You cannot ban yourself")
            return
        if reason == None:
            reason = "For being a jerk!"
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        #await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} is banned!")

    #The below code unbans player.
    @commands.command(pass_context=True)
    @commands.has_any_role(983975830868860958)
    async def unban(bot, ctx, id: int):
        user = await ctx.bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}')

    @commands.command(pass_context=True)
    @commands.has_any_role(983975830868860958)
    async def kick(bot, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has kicked.')

    @commands.command(pass_context=True)
    @commands.has_any_role(983975830868860958)
    async def mute(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        role = get(ctx.guild.roles, id=983975799256399872)
        await member.add_roles(role, atomic=True)
        await ctx.send(f'User {member} has been muted.')
        if reason != None:
          await ctx.send(f'Reason:{reason}')

    @commands.command(pass_context=True)
    @commands.has_any_role(983975830868860958)
    async def unmute(self, ctx: commands.Context, member: discord.Member):
        role = get(ctx.guild.roles, id=983975799256399872)
        await member.remove_roles(role, atomic=True)
        await ctx.send(f'User {member} has been unmuted.')


    @commands.command(pass_context = True)
    async def key(self, ctx: commands.Context, member: discord.Member = None):
        if member == None:
          author = ctx.author.id
          print(author)
        else:
          author = member.id
          print (author)

        user = ctx.bot.get_user(author)

        def writeJson(data, filename="users.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

                
        with open("users.json", "r") as f:
            data = json.load(f)
            nogger = 0
            i = 0
            for person in data['users']:
                i += 1
                if author == person["userid"]:
                    print('yes')
                    if "week" in person["type"]:
                        datey = person["time"]
                        date_obj = datetime.strptime(
                            datey, "%Y-%m-%d, %H:%M:%S")
                        now3 = datetime.now()
                        time_change = timedelta(days=7)
                        new_time = date_obj + time_change
                        print(new_time)
                        if new_time < now3:
                            embed = discord.Embed(
                            title="Information",
                            description=f"The license from {user.name} is invalid!",
                            color=0xDC143C)
                            print("invalid")
                            await ctx.send(embed=embed)
                            data['users'].remove(person)
                            writeJson(data)
                            return
                        else:
                            embed = discord.Embed(
                            title=f"Information from {user.name}",
                            description=f"Key redeemed: ```{datey}```\nKey valid until: ```{new_time}```\n License type: ```Weekly Access```",
                            color=0x7FFF00)
                            await ctx.send(embed=embed)
                            print('valid')
                            nogger = 1
                            return
                           

                    elif "month" in person["type"]:
                        datey = person["time"]
                        date_obj = datetime.strptime(
                            datey, "%Y-%m-%d, %H:%M:%S")
                        now3 = datetime.now()
                        time_change = timedelta(days=30)
                        new_time = date_obj + time_change
                        print(new_time)
                        if new_time < now3:
                            embed = discord.Embed(
                            title="Information",
                            description=f"The license from {user.name} is invalid!",
                            color=0xDC143C)
                            print("invalid")
                            await ctx.send(embed=embed)
                            data['users'].remove(person)
                            writeJson(data)
                            return
                        else:
                            embed = discord.Embed(
                            title=f"Information from {user.name}",
                            description=f"Key redeemed: ```{datey}```\nKey valid until: ```{new_time}```\n License type: ```Monthly Access```",
                            color=0x7FFF00)
                            await ctx.send(embed=embed)
                            print('valid')
                            nogger = 1
                            return
                            

                    elif "life" in person["type"]:
                        datey = person["time"]
                        date_obj = datetime.strptime(
                            datey, "%Y-%m-%d, %H:%M:%S")
                        now3 = datetime.now()
                        time_change = timedelta(days=9999)
                        new_time = date_obj + time_change
                        print(new_time)
                        if new_time < now3:
                            embed = discord.Embed(
                            title="Information",
                            description=f"The license from {user.name} is invalid!",
                            color=0xDC143C)
                            print("invalid")
                            await ctx.send(embed=embed)
                            data['users'].remove(person)
                            writeJson(data)
                            return
                        else:
                            embed = discord.Embed(
                            title=f"Information from {user.name}",
                            description=f"Key redeemed: ```{datey}```\nKey valid until: ```{new_time}```\n License type: ```Lifetime Access```",
                            color=0x7FFF00)
                            await ctx.send(embed=embed)
                            print('valid')
                            nogger = 1
                            return
                        break
            if nogger == 0:
                print("nein")
                embed = discord.Embed(title="Information", description=f"The User **{user.name}** does not own a valid license!", color=0xDC143C)
                await ctx.send(embed=embed)


    @commands.command(name = "time")
    async def time (self, ctx):
          now = datetime.now() + timedelta(hours=0)
          jetzt = now.strftime(f'%H:%M:%S')
          jetzt2 = now.strftime(f'%I:%M %p')
          print(jetzt)
          embed = discord.Embed(title=f"Current Server Time", description=f"**{jetzt2}**\n Für die Deutschen:\n**{jetzt}**", color=0x7FFF00)
          await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def replace (ctx, member:discord.User=None):
        message = f"https://cdn.discordapp.com/attachments/939820990156931092/939821475282685963/unknown-55.png \n please do it exactly as shown in the picture!" 
        await member.send(message)

    @commands.command(pass_context=True)
    async def btc (ctx, member:discord.User=None):
        await member.send("bc1qujeudrlpv34ngfp2dey8jphgk54r8swtfyj8dx")

    @commands.command(pass_context=True)
    async def eth (ctx, member:discord.User=None):
        await member.send("0x06E39ac62299b7cB046b404E4208d4859D0B03e7")

    @commands.command(pass_context=True)
    async def ltc (ctx, member:discord.User=None):
        await member.send("LQ36yjUvXVfzMPoqGBuga9o6YPL56c43bq")

    @commands.command(pass_context=True)
    async def rep (self, ctx:commands.Context):
        await ctx.send("pls write a positiv reputation in channel: <#905492842770747472>")
        await ctx.message.delete(delay=1)
      
    @commands.command(pass_context=True)
    async def webm (self, ctx:commands.Context):
        await ctx.send(f"https://crx-gen.xyz/ \nhere is our webmail for the accounts!")
        await ctx.message.delete(delay=1)
      
    @commands.command(name = "vorlage")
    async def vorlage (self, ctx: commands.Context, member:discord.User=None):
        embed = discord.Embed(title="Replacement Template", description=f" ", color=0x800000)
        embed.add_field(name="Instructions", value="Please send a screenshot like the picture below", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/937684881104830544/937704809698582588/unknown-55.png"
        )
        await ctx.send(embed=embed)
        await ctx.message.delete(delay=1)
def setup(bot: commands.Bot):
    bot.add_cog(Vorlage(bot))
