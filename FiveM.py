from discord.ext import commands  # Again, we need this imported
import discord

import asyncio
import os
import datetime
import time


class FiveM(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['fivem'])
    @commands.has_any_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def FiveM(self, ctx: commands.Context, amount=""):

      if amount == "":
                f = open("accounts.txt", "r")
                count = len(open("accounts.txt").readlines())
                print(count)
                f.close()

                if count == 0:
                  await ctx.send ("No more accounts!")
                  return

                f = open("accounts.txt")
                firstline = f.readline()
                f.close()

                now = datetime.datetime.now()
                now2 = now.strftime("%Y-%m-%d, %H:%M:%S")
                
                f3 = open("logs.txt", "r+")
                f3.seek(0, os.SEEK_END)
                f3.writelines(f"FiveM get: {ctx.author.display_name}, {now2}")
                f3.writelines("\n")
                f3.close()

                embed = discord.Embed(title="Your Account",
                                  description=f"||{firstline}||",
                                  color=0xE67E22)
                embed.set_author(name=f"Command run by {ctx.author.display_name}",
                             icon_url=ctx.author.avatar_url)

                f = open("accounts.txt", "r+")

                f4 = open("backup.txt", "r+")
                f4.seek(0, os.SEEK_END)
                f4.writelines(f"FiveM-- {firstline}")
                f4.close
                lines = f.readlines()
                #Move to first line
                f.seek(0)
                #truncate
                f.truncate()

                #Start writing skipping line 1
                f.writelines(lines[1:])
                f.close()

                f = open("accounts.txt")
                count2 = len(open("accounts.txt").readlines())
                print(count2)
                f.close()
                embed.set_footer(text=f"{count2} accounts left!")

                await ctx.send(embed=embed)
                time.sleep(1)

                return

      try:
            amount = int(amount)
            #await ctx.send ("int")
            member = ctx.author
            if 907977756850155560 in [y.id for y in member.roles]:
              amount = 1
              ctx.send(f"{member.mention} Supporters can only generate 1 Account!", delete_after=10)
            if amount > 5:
              if 921013889964068865 in [y.id for y in member.roles]:
                amount = 5
                ctx.send(f"{member.mention} Users with the Bot 1 Role can only generate 5 Accounts!", delete_after=10)
              if 903699777613627472 in [y.id for y in member.roles]:
                amount = 10
                ctx.send(f"{member.mention} Administrators can only generate 10 Accounts!", delete_after=10)
            else:
              for x in range(0, amount):

                f = open("accounts.txt", "r")
                count = len(open("accounts.txt").readlines())
                print(count)
                f.close()

                if count == 0:
                    await ctx.send ("No more accounts!")
                    break

                f = open("accounts.txt") 
                firstline = f.readline()
                f.close()

                now = datetime.datetime.now()
                now2 = now.strftime("%Y-%m-%d, %H:%M:%S")

                f3 = open("logs.txt", "r+")
                f3.seek(0, os.SEEK_END)
                f3.writelines(f"FiveM get: {ctx.author.display_name}, {now2}")
                f3.writelines("\n")
                f3.close()

                embed = discord.Embed(title="Your Account",
                                  description=f"||{firstline}||",
                                  color=0xE67E22)
                embed.set_author(name=f"Command run by {ctx.author.display_name}",
                             icon_url=ctx.author.avatar_url)

                f = open("accounts.txt", "r+")

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
                f4.writelines(f"FiveM-- {firstline}")
                f4.close
                f = open("accounts.txt")
                count2 = len(open("accounts.txt").readlines())
                print(count2)
                f.close()
                embed.set_footer(text=f"{count2} Accounts left!")

                await ctx.send(embed=embed)

      except ValueError:
                await ctx.send ("Amount of accounts has to be a Number!", delete_after=5)



def setup(bot: commands.Bot):
    bot.add_cog(FiveM(bot))
