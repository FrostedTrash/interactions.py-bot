from discord.ext import commands  # Again, we need this imported

import interactions
from interactions.ext.get import get

import time

global guild_id
global staff_role
global owner_role

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263

class deletecommand(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="del",
        description="Deletes the current channel",
    )
    async def delete(self, ctx: interactions.CommandContext):
        if owner_role in ctx.author.roles:
            await ctx.send("Channel will be deleted shortly...", components=None)
            time.sleep(3)
            channel = await ctx.get_channel()
            guild = await ctx.get_guild()
            await guild.delete_channel(channel_id=channel.id)
        else:
            owner = await get(self.bot, interactions.Role, guild_id=guild_id, role_id=owner_role)
            embed = interactions.Embed(title="No Permission", description=f"You do not have the required {owner.mention} Role!", color=0xE74C3C)
            await ctx.send(embeds=embed)


def setup(client):
    deletecommand(client)
