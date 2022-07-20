from discord.ext import commands
import interactions

import time


class ticketrename(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="rename",
        description="Rename the current channel!",
        options = [
            interactions.Option(
                name="name",
                description="What you want the channel to be named",
                type=interactions.OptionType.STRING,
                required=True,
            ),
        ],
    )
    async def renameticket(self, ctx: interactions.CommandContext, name: str):
        channel = await ctx.get_channel()
        guild = await ctx.get_guild()

        await guild.modify_channel(channel_id=channel.id, name=name)
        msg = await ctx.send(f"Successfully renamed Channel to {channel.mention}!")
        time.sleep(3)
        await msg.delete()

def setup(client):
    ticketrename(client)