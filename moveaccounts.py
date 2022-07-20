from discord.ext import commands # Again, we need this imported
import discord #needed for Embeds

import datetime
import os

class moveaccounts(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="move")
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=10)
    async def move(self, ctx: commands.Context):
        with open("addedgtaaccounts.txt", "r+") as f:
          lines = f.read()
          print (lines)
          f.truncate(0)
        f2 = open("gtaaccounts.txt", "r+")
        f2.seek(0, os.SEEK_END)
        f2.writelines(f"{lines}")
        f2.close()

        with open("addedfivemaccounts.txt", "r+") as f:
          lines2 = f.read()
          print (lines)
          f.truncate(0)
        f2 = open("accounts.txt", "r+")
        f2.seek(0, os.SEEK_END)
        f2.writelines(f"{lines2}")
        f2.close()

        now = datetime.datetime.now()
        now2 = now.strftime("%Y-%m-%d, %H:%M:%S")          

        f3 = open("logs.txt", "r+")
        f3.seek(0, os.SEEK_END)
        f3.writelines(f"Move Accounts: {ctx.author.display_name}, {now2}")
        f3.writelines("\n")
        f3.close()

        embed = discord.Embed(title="Moved!", description=f"Moved the following accounts!\n **GTA:**\n {lines}\n **FiveM:**\n {lines2}", color=0x2E8B57)
        embed.set_author(name=f"Command run by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        


def setup(bot: commands.Bot):
    bot.add_cog(moveaccounts(bot))