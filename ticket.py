import asyncio
import datetime
import email
from email import message
import json
import os
import time
from ast import Return
from cgitb import text
from cProfile import label
from turtle import title
from typing import List, Union
from unicodedata import name

import discord
import interactions
import requests
from click import style
from discord.ext import commands  # Again, we need this imported
from interactions.ext.get import get

import re


global guild_id
global staff_role
global owner_role

guild_id = 921350023885758465
staff_role = 985243571630252107
owner_role = 922247919711711263

class ticket(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="button",
        description="Button test allah"
    )
    async def button(self, ctx: interactions.CommandContext):
        button = interactions.Button(
            style=interactions.ButtonStyle.SUCCESS,
        	label="Buy",
        	custom_id="buy",
            emoji = interactions.Emoji(name="💸")
        )
        button2 = interactions.Button(
            style=interactions.ButtonStyle.DANGER,
            label="Support",
            custom_id="support",
            emoji = interactions.Emoji(name="❓")
        )
        button3 = interactions.Button(
            style=interactions.ButtonStyle.PRIMARY,
            label="Giveaway",
            custom_id="giveaway",
            emoji=interactions.Emoji(name="🎉")
        )
        row = interactions.ActionRow(
            components=[button, button2, button3]
        )
        embed = interactions.Embed(title="Open a Ticket", description="If you want to open a Ticket please choose one of the preferred main Categories!\n\nPlease also make sure to check out our Payment Methods before Ordering!")
        embed.add_field(name="**Payment Methods**", value="<a:aNeonArrowRight:909397663630364712> PayPal\n<a:aNeonArrowRight:909397663630364712> Paysafecard (fee)\n<a:aNeonArrowRight:909397663630364712> Crypto (BTC, LTC, ETH)\n<a:aNeonArrowRight:909397663630364712> Tipeeestream Donations (fee)")
        await ctx.send(embeds=embed, components=row)

    @interactions.extension_component("support")
    async def support_response(self, ctx: interactions.CommandContext):
        #print(staff)
        option = [interactions.SelectOption(
            label="General Support",
            value="general",
            description="Use this to get general Support without any specific topic",
            emoji = interactions.Emoji(name="❓")
        ),
        interactions.SelectOption(
            label="FiveM | GTA | Red Dead Redemption2",
            value="account_sup",
            description="Use this if you need support for Accounts!",
            emoji = interactions.Emoji(name="❓")
        )
        ]
        menu = interactions.SelectMenu(
            options=option,
            placeholder="Please choose one of the options!",
            custom_id="menu_support",
        )
        msg = await ctx.send(components=menu, ephemeral=True)

    @interactions.extension_component("buy")
    async def buy_response(self, ctx: interactions.CommandContext):
        #print(staff)
        option = [interactions.SelectOption(
            label="FiveM | GTA | Red Dead Redemption2",
            value="account1_buy",
            description="Use this if you want to buy one of the 3 Accounts",
            emoji = interactions.Emoji(id=909480306267025468, animated=True)
        )
        ]
        menu = interactions.SelectMenu(
            options=option,
            placeholder="Please choose one of the options!",
            custom_id="menu_support",
        )
        msg = await ctx.send(components=menu, ephemeral=True)

    @interactions.extension_component("giveaway")
    async def giveaway_response(self, ctx: interactions.CommandContext):
        #print(staff)
        option = [interactions.SelectOption(
            label="Nitro win",
            value="nitro_win",
            description="Use this to claim your Nitro!",
            emoji = interactions.Emoji(name="🎉")
        ),
        interactions.SelectOption(
            label="FiveM | GTA | RDR2 win",
            value="account_win",
            description="Use this to claim your Account(s)!",
            emoji = interactions.Emoji(name="🎉")
        ),
        interactions.SelectOption(
            label="Other win",
            value="other_win",
            description="Use this to claim your Giveaway price!",
            emoji = interactions.Emoji(name="🎉")
        )
        ]
        menu = interactions.SelectMenu(
            options=option,
            placeholder="Please choose one of the options!",
            custom_id="menu_support",
        )
        msg = await ctx.send(components=menu, ephemeral=True)
        

    @interactions.extension_component("close")
    async def close_response(self, ctx: interactions.CommandContext):
        message = await ctx.send("Ticket will be closed in a few seconds...")
        time.sleep(3)
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
        button_del = interactions.Button(
            style=interactions.ButtonStyle.DANGER,
            label="Delete",
        	custom_id="delete",
            emoji = interactions.Emoji(name="🗑️")
        )
        button_save = interactions.Button(
            style=interactions.ButtonStyle.SUCCESS,
            label="Save",
        	custom_id="save",
            emoji = interactions.Emoji(name="✅")
        )
        delbutton = interactions.ActionRow(
            components=[button_del, button_save]
        )
        embed = interactions.Embed(title="Ticket closed!", description=f"Ticket has been closed by {ctx.author.mention}", color=0xE74C3C)
        await message.edit(embeds=embed, components=delbutton)
    
    @interactions.extension_component("delete")
    async def del_response(self, ctx:interactions.CommandContext):
        await ctx.send("Ticket will be deleted shortly...", components=None)
        time.sleep(3)
        channel = await ctx.get_channel()
        guild = await ctx.get_guild()
        await guild.delete_channel(channel_id=channel.id)
    
    @interactions.extension_component("save")
    async def save_response(self, ctx:interactions.CommandContext):
        channel = await ctx.get_channel()
        history = await channel.get_history(limit=100)
        print(history)
        await ctx.send("Save geht noch nicht. Wenn wer tipps hat pls melden xd")
    
    @interactions.extension_component("menu_support")
    async def menu_response(self, ctx: interactions.CommandContext, value: str):
        async def createticket(self, ctx: interactions.CommandContext, name: str, type: str):
            guild = await ctx.get_guild()
            member = ctx.author
            if type == "Nitro":
                staff = await get(self.bot, interactions.Role, guild_id=guild_id, role_id=owner_role)
            else:
                staff = await get(self.bot, interactions.Role, guild_id=guild_id, role_id=staff_role)
            overwrites = []
            overwrites.append(interactions.Overwrite(
                id = int(guild.id),
                type = 0,
                deny = interactions.Permissions.VIEW_CHANNEL,
            ))
            overwrites.append(interactions.Overwrite(
                id = int(ctx.author.id),
                type = 1,
                allow = interactions.Permissions.VIEW_CHANNEL | interactions.Permissions.SEND_MESSAGES
            ))
            overwrites.append(interactions.Overwrite(
                id = int(staff.id),
                type = 0,
                allow = interactions.Permissions.VIEW_CHANNEL | interactions.Permissions.SEND_MESSAGES
            ))
            channel = await guild.create_channel(name=f"{type}-{name}-{member.name}", type=interactions.ChannelType.GUILD_TEXT, permission_overwrites=overwrites)
            button_close = interactions.Button(
                style=interactions.ButtonStyle.DANGER,
        	    label="Close",
        	    custom_id="close",
                emoji = interactions.Emoji(name="❎")
            )
            closebutton = interactions.ActionRow(
                components=[button_close]
            )
            #channel = await guild.create_channel(f"Support-{member.name}", overwrites=overwrites, category=discord.utils.get(ctx.guild.categories, id=984513720820588614))
            embed = interactions.Embed(title=f"{type} {name} Ticket from {member.name}!", description=f"Hello!\n Please wait patiently a {staff.mention} will be with you shortly!\nIn the meantime you can already describe your Issue here.\n \nYou can close this Ticket by running the **/close** command!\nOr use the Button below!")
            await channel.send(embeds=embed, components=closebutton)
            await ctx.send(f"You have opened a {type} {name} Ticket!\nYou can find it here! {channel.mention}", ephemeral=True)
        print(value)
        if "general" in value:
            await createticket(self, ctx, "Support", "general")
        elif "account_sup" in value:
            await createticket(self, ctx, "Support", "Account")
        elif "account_buy" in value:
            await createticket(self, ctx, "Buy", "Account")
        elif "nitro_win" in value:
            await createticket(self, ctx, "Giveaway", "Nitro")
        elif "account_win" in value:
            await createticket(self, ctx, "Giveaway", "Account")
        elif "other_win" in value:
            await createticket(self, ctx, "Giveaway", "Other")
        
def setup(client):
    ticket(client)
