from discord.ext import commands # Again, we need this imported
import discord

class GTAlist(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['gstock'])
    @commands.cooldown(rate=1, per=10)
    async def stockg(self, ctx: commands.Context):
        count = len(open("gtaaccounts.txt").readlines())
        embed = discord.Embed(title=f"{count} GTA Downloadable Accounts in total!", color=0xE67E22)
        embed.set_author(name=f"Command run by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(GTAlist(bot))