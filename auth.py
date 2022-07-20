import discord

import interactions
from interactions.ext.get import get

global logging

logging = True

#Trashy was here
class auth_cmd(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="auth",
        description="Send Authentication Button",
        scope= 997250141973135501 #961745188655603732 <- Rein DC 921350023885758465 <- Test DC 997250141973135501 <- Main DC
    )
    async def auth_cmd(self, ctx: interactions.CommandContext):
        button = interactions.Button(
            style=interactions.ButtonStyle.SUCCESS,
        	label="Verify!",
        	custom_id="auth",
            #emoji = interactions.Emoji(name="✅​")
        )

        embed = interactions.Embed(title="Authentication!", description="If you want to get Verified click the '**Verify!**' Button below!", color=0xB533FF)
        channel = await ctx.get_channel()
        await channel.send(embeds=embed, components=button)
        await ctx.send("Auth sent", ephemeral=True)
    
    @interactions.extension_component("auth")
    async def auth_response(self, ctx: interactions.CommandContext):
        await ctx.author.add_role(role=997250141973135509, guild_id=997250141973135501, reason="autorole")
        await ctx.send("You have been verified!", ephemeral=True)
        if logging:
            channel = await get(self.bot, interactions.Channel, channel_id=997503760442064928)
            await channel.send(f"{ctx.author.mention} has been verified!")


#Made by Trashy#0187
def setup(client):
    auth_cmd(client)
