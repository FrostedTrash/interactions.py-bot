from discord.ext import commands  # Again, we need this imported
import discord

import asyncio
import os
import datetime
import json


class FiveM(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2)
    async def gen(self, ctx: commands.Context):
        if ctx.channel.id != 922833104345899009:
            await ctx.message.delete(delay=5)
            await ctx.send("Wrong Channel!", delete_after=5)
            return
        author = ctx.author.id
        print(author)
        f = open("gen.txt", "r")
        lines = f.read()
        amount = lines.count(str(author))
        print(amount)
        f.close()

        def writeJson(data, filename="users.json"):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        with open("users.json", "r") as f:
            nigga = "False"
            data = json.load(f)
            i = 0
            for person in data['users']:
                i += 1
                if ctx.message.author.id == person["userid"]:
                    print('yes')
                    if "week" in person["type"]:
                        datey = person["time"]
                        date_obj = datetime.datetime.strptime(
                            datey, "%Y-%m-%d, %H:%M:%S")
                        now3 = datetime.datetime.now()
                        time_change = datetime.timedelta(days=7)
                        new_time = date_obj + time_change
                        print(new_time)
                        if new_time < now3:
                            print("invalid")
                            data['users'].remove(person)
                            writeJson(data)
                        else:
                            print('valid')
                            nigga = "True"

                    elif "month" in person["type"]:
                        datey = person["time"]
                        date_obj = datetime.datetime.strptime(
                            datey, "%Y-%m-%d, %H:%M:%S")
                        now3 = datetime.datetime.now()
                        time_change = datetime.timedelta(days=30)
                        new_time = date_obj + time_change
                        print(new_time)
                        if new_time < now3:
                            print("invalid")
                            data['users'].remove(person)
                            writeJson(data)
                        else:
                            print('valid')
                            nigga = "True"

                    elif "life" in person["type"]:
                        datey = person["time"]
                        date_obj = datetime.datetime.strptime(
                            datey, "%Y-%m-%d, %H:%M:%S")
                        now3 = datetime.datetime.now()
                        time_change = datetime.timedelta(days=9999)
                        new_time = date_obj + time_change
                        print(new_time)
                        if new_time < now3:
                            print("invalid")
                            data['users'].remove(person)
                            writeJson(data)
                        else:
                            print('valid')
                            nigga = "True"
                    break
            if nigga == "True":
                if amount < 5:
                    f = open("gen.txt", "r+")
                    f.seek(0, os.SEEK_END)
                    f.writelines(f"{author}")
                    f.writelines("\n")  #hier muss dann das mit dm rein
                    f.close()

                    f = open("accounts.txt", "r")
                    count = len(open("accounts.txt").readlines())
                    print(count)
                    f.close()

                    if count == 0:
                        await ctx.send(f"{ctx.author.mention}No more accounts!"
                                       )
                        return

                    f = open("accounts.txt")
                    firstline = f.readline()
                    f.close()

                    embed = discord.Embed(title="Your Account",
                                          description=f"||{firstline}||",
                                          color=0xE67E22)

                    f = open("accounts.txt", "r+")

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
                    embed.set_footer(text=f"{count2} Accounts left!")

                    await ctx.send(f"{ctx.author.mention} Check DMs!")
                    await ctx.author.send(embed=embed)
                    return

                else:
                    embed = discord.Embed(
                        title="Account limit for today reached!",
                        description=
                        "You will be able to generate more after 12:00 A.M!",
                        color=0xE74C3C)
                    await ctx.send(embed=embed)
                    return

            else:
                embed = discord.Embed(
                    title="Error",
                    description=f"You dont have a valid license!",
                    color=0xE74C3C)
                await ctx.send(embed=embed)
                return


def setup(bot: commands.Bot):
    bot.add_cog(FiveM(bot))
