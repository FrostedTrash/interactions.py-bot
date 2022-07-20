from discord.ext import commands # Again, we need this imported
import discord

import interactions
from interactions.ext.get import get


global guild_id
global staff_role
global owner_role
global customer_role
global channel_id
global channel2_id
global welcome_id

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263

customer_role = 922391127976472626
channel_id = 932284659730120804
channel2_id = 922482838266335312
welcome_id = 986389984871329873

class memberjoin(interactions.Extension):
    """A couple of simple commands."""
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_listener()
    async def on_guild_member_add(self, member: interactions.Member):
      _member = await get(self.bot, interactions.Member, guild_id=guild_id, member_id=member.id)
      role = await get(self.bot, interactions.Role, guild_id=guild_id, role_id=customer_role)
      #await member.add_role(role=role, reason="Autorole")
      channel = await get(self.bot, interactions.Channel, channel_id=channel_id) #Channel ID wo er das reinschickt
      channel2 = await get(self.bot, interactions.Channel, channel_id=channel2_id)
      welcome = await get(self.bot, interactions.Channel, channel_id=welcome_id)

      if not channel:
        return

      await channel.send(f"{member.mention}")
      await channel2.send(f"{member.mention}")
      embed = interactions.Embed(title="Welcome!", description=f"Welcome {member.mention}!\nMake sure to have a look at <#983975901844881419> and <#983975920945745931>!\nEnjoy your stay!", colour=0xE74C3C)
      embed.set_thumbnail(url=member.user.avatar_url)
      await welcome.send(embeds=embed)
      await channel.delete()
      await channel2.delete()

    @interactions.extension_listener()
    async def on_guild_member_remove(self, member: interactions.GuildMember):
      leave = await get(self.bot, interactions.Channel, channel_id=welcome_id)

      if not leave:
        return

      _member = await get(self.bot, interactions.Member, guild_id=guild_id, member_id=member.id)
      print(_member.get_member_avatar_url(guild_id=guild_id))
      embed = interactions.Embed(title="Good Bye!", description=f"Sadly {member.mention} left us!\nThanks for Joining and staying here!\nSee you next time :)", colour=0xE74C3C)
      embed.set_thumbnail(url=_member.user.avatar_url)
      await leave.send(embeds=embed)
      

def setup(client):
    memberjoin(client)