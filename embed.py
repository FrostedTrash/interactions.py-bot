from discord.ext import commands  # Again, we need this imported
import discord


class embed(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="embed")
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def embed(self, ctx: commands.Context):

        embed = discord.Embed(title="", colour=0x7289DA)
        embed.add_field(
            name= """Rulebook""",
            value=
            """
                <a:aNeonArrowRight:909397663630364712> **Bots**\n
                > Any form of Discord bots are only allowed after consultation with team members or Discord administrators.\n
                <a:aNeonArrowRight:909397663630364712> **Level protection**\n
                > To ensure the level, we reserve the right to ban people for a limited time or permanently.\n
                <a:aNeonArrowRight:909397663630364712> **Advertising**\n
                > Advertising on this Discord server for other projects/servers is strictly prohibited. This includes writing to people via private message and then advertising there.\n
                > Any sending of cheats / hacks / executors / mod menus / spoofers is prohibited.\n
                > Advertising cheats / hacks / executors / mod menus / spoofers is also prohibited.\n
                **The resale of our products is prohibited and we will act accordingly.**\n
                **ATTENTION: There are no refunds!**
""",
            inline=False)


        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(embed(bot))
