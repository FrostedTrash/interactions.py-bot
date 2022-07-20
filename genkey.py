from discord.ext import commands  # Again, we need this imported
import discord
from discord.utils import get
import os
import random
import string
from datetime import datetime, timedelta

#Trashy war hier
class key(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['rr'])
    @commands.has_any_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def redem(self, ctx: commands.Context, arg: str):

          print(len(arg))
          if (len(arg)) < 16:
              print("False")
              embed = discord.Embed(
                title="Error",
                description="Invalid Key!",
                color=0xDC143C)

              await ctx.send(embed=embed)
          else:
              if (len(arg)) == 17:
                f = open("genkey.txt", "r+")
                lines = f.read()
                if arg in lines:
                      f.truncate(0)
                      f.close()
                      print("True")
                      member = ctx.author
                      role = get(ctx.guild.roles, id=929765076095860768)
                      await member.add_roles(role, atomic=True)
                      channel = self.bot.get_channel(929472239055810560)
                      await channel.send(embed = discord.Embed(
                            title="LOG",
                            description=f"{ctx.author.mention} hat einen 7 Tage Key eingelöst!",
                            color=0x2E8B57))
                      author = ctx.author
                      now = datetime.now() + timedelta(days=0)
                      now1 = datetime.now() + timedelta(days=1)
                      now2 = datetime.now() + timedelta(days=2)
                      now3 = datetime.now() + timedelta(days=3)
                      now4 = datetime.now() + timedelta(days=4)
                      now5 = datetime.now() + timedelta(days=5)
                      now6 = datetime.now() + timedelta(days=6)
                      print(now)
                      jetzt = now.strftime(f'%Y-%m-%d')
                      jetzt1 = now1.strftime(f'%Y-%m-%d')
                      jetzt2 = now2.strftime(f'%Y-%m-%d')
                      jetzt3 = now3.strftime(f'%Y-%m-%d')
                      jetzt4 = now4.strftime(f'%Y-%m-%d')
                      jetzt5 = now5.strftime(f'%Y-%m-%d')
                      jetzt6 = now6.strftime(f'%Y-%m-%d')
                      print(jetzt6)
                      embed = discord.Embed(
                        title="Success!",
                        description=
                        "Your 1 week key, **Generator Access**, has been successfully redeemed",
                        color=0x2E8B57)
                      await ctx.send(embed=embed)
                      embed = discord.Embed(
                        title="Success!",
                        description=
                        f"Your 1 week key, is valid ago **{jetzt6}**",
                        color=0x2E8B57)
                      await ctx.send(embed=embed)
                      f88 = open("genacces.txt", "r+")
                      f88.seek(0, os.SEEK_END)
                      f88.writelines(f"{author} {str(jetzt)}\n")
                      f88.writelines(f"{author} {str(jetzt1)}\n")
                      f88.writelines(f"{author} {str(jetzt2)}\n")
                      f88.writelines(f"{author} {str(jetzt3)}\n")
                      f88.writelines(f"{author} {str(jetzt4)}\n")
                      f88.writelines(f"{author} {str(jetzt5)}\n")
                      f88.writelines(f"{author} {str(jetzt6)}\n")
                
                      f88.close()

                
                else: 
                  embed = discord.Embed(
                        title="Success!",
                        description=
                        "Your key isn't valid!",
                        color=0xE83845)
                  f.close()
                  await ctx.send(embed=embed)
                  
              elif (len(arg)) == 18:
                    f2 = open("genkey.txt", "r+")
                    lines = f2.read()
                    if arg in lines:
                      f2.truncate(0)
                      f2.close()
                      print("lifetime")
                      embed = discord.Embed(
                        title="Success!",
                        description=
                        "Your LIFETIME key was redeemed!",
                        color=0x2E8B57)
                      embed.set_author(
                        name=f"Key redeemed by {ctx.author.display_name}",
                        icon_url=ctx.author.avatar_url)
                      await ctx.send(embed=embed)
                      member = ctx.author
                      role = get(ctx.guild.roles, id=929067935786500158)
                      await member.add_roles(role, atomic=True)
                      channel = self.bot.get_channel(929472239055810560)
                      await channel.send(embed = discord.Embed(
                            title="LOG",
                            description=f"{ctx.author.display_name} hat einen Lifetime Key eingelöst!",
                            color=0x2E8B57))
                    else: 
                      embed = discord.Embed(
                        title="Success!",
                        description=
                        "Your Key isn't valid!",
                        color=0x2E8B57)
                      f2.close()
                      await ctx.send(embed=embed)


    @commands.command(name="genkey7")
    @commands.has_any_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def genkey7(self, ctx: commands.Context):

        S = 17  # number of characters in the string.
        # call random.choices() string module to find the string in Uppercase + numeric data.
        ran = ''.join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=S))

        f3 = open("genkey.txt", "r+")
        f3.seek(0, os.SEEK_END)
        f3.writelines(f"{ran} \n")
        f3.close()

        embed = discord.Embed(
            title="Your __Demon Gen__ Month Key",
            description=f"||{ran}||\nUse it by writing ***r KEY** in this Ticket!",
            color=0xBA55D3)
        embed.set_author(name=f"Command run by {ctx.author.display_name}",
                         icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(name="genkeyl")
    @commands.has_any_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def genkeyl(self, ctx: commands.Context):

        S = 18  # number of characters in the string.
        # call random.choices() string module to find the string in Uppercase + numeric data.
        ran = ''.join(
            random.choices(string.ascii_uppercase + string.digits +
                           string.ascii_lowercase,
                           k=S))

        f4 = open("genkey.txt", "r+")
        f4.seek(0, os.SEEK_END)
        f4.writelines(f"{ran} \n")
        f4.close()

        embed = discord.Embed(
            title="Your __Demon Gen__ Lifetime Key",
            description=f"||{ran}||\nUse it by writing ***r KEY** in this Ticket!",
            color=0xBA55D3)
        embed.set_author(name=f"Command run by {ctx.author.display_name}",
                         icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)
#Made by Kxmi#6666
def setup(bot: commands.Bot):
    bot.add_cog(key(bot))
