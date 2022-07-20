from discord.ext import commands
import interactions
from interactions.ext.get import get

import re

global staff_role
global owner_role
global guild_id

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263


class closeticket(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="close",
        description="Closes the current ticket!",
    )
    async def close_command(self, ctx: interactions.CommandContext):
        channel = await ctx.get_channel()
        guild = await ctx.get_guild()
        staff = await get(self.bot, interactions.Role, guild_id=guild_id, role_id=staff_role)


        channel.permission_overwrites.clear()
        print(channel.permission_overwrites)
        print(channel.name)
        name = channel.name
        name = re.sub(r'^.*?-', 'closed-', name)
        print(name)
        overwrites = []
        overwrites.append(interactions.Overwrite(
            id = int(guild.id),
            type = 0,
            deny = interactions.Permissions.VIEW_CHANNEL,
        ))
        overwrites.append(interactions.Overwrite(
            id = int(staff.id),
            type = 0,
            allow = interactions.Permissions.VIEW_CHANNEL | interactions.Permissions.SEND_MESSAGES
        ))
        await guild.modify_channel(channel_id=channel.id, name=name, permission_overwrites=overwrites)
        embed = interactions.Embed(title="Ticket closed!", description=f"Ticket has been closed by {ctx.author.mention}", color=0xE74C3C)
        await ctx.send(embeds=embed)

        
           

def setup(client):
    closeticket(client)