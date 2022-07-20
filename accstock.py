from unicodedata import name
from discord.ext import commands # Again, we need this imported
import discord
import interactions

class accstock(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="stock",
        description="Shows the Stock of one of the Options",
        options = [
            interactions.Option(
                name="account",
                description="Choose one of the 3 Accounts",
                type=interactions.OptionType.STRING,
                required=True,
                choices=[
                    interactions.Choice(
                        name = "FiveM",
                        value = "fivem",
                    ),
                    interactions.Choice(
                        name="GTA Downloadable",
                        value="gta",
                    ),
                    interactions.Choice(
                        name="RDR2",
                        value="rdr",
                    ),
                ],
            ),
        ],
    )
    async def accs(self, ctx: interactions.CommandContext, account: str):
        if account == "rdr":
            count = len(open("reddead.txt").readlines())
            embed = interactions.Embed(title=f"{count} RDR2 Accounts in total!", color=0xE67E22)
            embed.set_author(name=f"Command run by {ctx.author.name}")
            await ctx.send(embeds=embed)
        elif account == "gta":
            count = len(open("gtaaccounts.txt").readlines())
            embed = interactions.Embed(title=f"{count} GTA 5 Accounts in total!", color=0xE67E22)
            embed.set_author(name=f"Command run by {ctx.author.name}")
            await ctx.send(embeds=embed)
        elif account == "fivem":
            count = len(open("accounts.txt").readlines())
            embed = interactions.Embed(title=f"{count} FiveM Accounts in total!", color=0xE67E22)
            embed.set_author(name=f"Command run by {ctx.author.name}")
            await ctx.send(embeds=embed)


def setup(client):
    accstock(client)