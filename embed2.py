from discord.ext import commands  # Again, we need this imported
import discord


class embed(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="embed2")
    @commands.has_role(983975830868860958)
    @commands.cooldown(rate=1, per=2)
    async def accounts(self, ctx: commands.Context):

        embed = discord.Embed(title="Discord Nitro", colour=0x7289DA)
        embed.add_field(
            name="Information",
            value=
            "Discord Nitro! \n Lifetime warranty if it gets revoked! \n Premium Support! \n Works in all countries!",
            inline=False)
        embed.add_field(name="Pricing",
                        value="``` **Nitro Classic** \n 1 Month -> 3€ \n 1 Year -> 10€ \n **Nitro Boost** \n 1 Month -> 5€ \n 1 Year -> 25€```",
                        inline=False)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/907956677217763338/920928076718813204/nitro_gif.gif"
        )

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(embed(bot))
