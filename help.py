from discord.ext import commands  # Again, we need this imported
import discord

import asyncio


class help1(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    print("1")

    @commands.command(name="help")
    @commands.cooldown(rate=1, per=5)
    async def help2(self, ctx: commands.Context):

        print("2")
        embed = discord.Embed(title="Help",
                              description="What help do you need?",
                              colour=0x1ABC9C)
        embed.set_author(name=f"Command run by {ctx.author.display_name}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name="Spoofing?",
                        value="Write 'spoofing'!",
                        inline=True)
        message = await ctx.send(embed=embed, delete_after=30)
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel

        try:
            confirm = await self.bot.wait_for("message",
                                              check=check,
                                              timeout=30)
        except asyncio.TimeoutError:
            embed = discord.Embed(
                title="Timeout",
                description="Timeout Error because Idle for over 30 seconds",
                colour=0xE74C3C)
            await ctx.send(embed=embed, delete_after=5)
            await message.delete()
            return

        if confirm.content == "spoofing":
            print("3")
            embed = discord.Embed(title="Spoofing Help",
                                  description="What type of help do you need?",
                                  colour=0x1ABC9C)
            embed.set_author(name=f"Command run by {ctx.author.display_name}",
                             icon_url=ctx.author.avatar_url)
            embed.add_field(name="Server Ban",
                            value="Write 'server'!",
                            inline=True)
            embed.add_field(name="Global",
                            value="Write 'global'!",
                            inline=True)
            embed.add_field(name="_01 Ban", value="Write '_01'!", inline=True)
            embed.add_field(name="NVME_M2 Method",
                            value="Write 'nvme_m2'!",
                            inline=True)
            embed.add_field(name="Reinstall Method",
                            value="Write 'reinstall'!",
                            inline=True)
            embed.add_field(name="Vanity Method",
                            value="Write 'vanity'!",
                            inline=True)                
            message = await ctx.send(embed=embed, delete_after=30)
            check = lambda m: m.author == ctx.author and m.channel == ctx.channel

            try:
                confirm = await self.bot.wait_for("message",
                                                  check=check,
                                                  timeout=30)
            except asyncio.TymeoutError:
                embed = discord.Embed(
                    title="Timeout",
                    description=
                    "Timeout Error because Idle for over 30 seconds",
                    colour=0xE74C3C)
                await ctx.send(embed=embed, delete_after=5)
                await message.delete()

            if confirm.content == "server":
                f = open("serverunban.txt")
                lines = f.read()
                f.close()
                embed = discord.Embed(title="Server unban",
                                      description=f"{lines}",
                                      colour=0x1ABC9C)
                embed.set_author(
                    name=f"Command run by {ctx.author.display_name}",
                    icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                await message.delete()
                return

            elif confirm.content == "global":
                f = open("globalunban.txt")
                lines = f.read()
                f.close()
                embed = discord.Embed(title="Global unban",
                                      description=f"{lines}",
                                      colour=0x1ABC9C)
                embed.set_author(
                    name=f"Command run by {ctx.author.display_name}",
                    icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                await message.delete()
                return

            elif confirm.content == "_01":
                f = open("_01unban.txt")
                lines = f.read()
                f.close()
                embed = discord.Embed(title="_01 unban",
                                      description=f"{lines}",
                                      colour=0x1ABC9C)
                embed.set_author(
                    name=f"Command run by {ctx.author.display_name}",
                    icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                await message.delete()
                return

            elif confirm.content == "nvme_m2":
                f = open("nvme_m2.txt")
                lines = f.read()
                f.close()
                f = open("nvme_m2_2.txt")
                lines2 = f.read()
                f.close()
                embed = discord.Embed(title="NVME M2 Method",
                                      description=f"{lines}",
                                      colour=0x1ABC9C)
                embed2 = discord.Embed(description=f"{lines2}", color=0x1ABC9C)
                embed.set_author(
                    name=f"Command run by {ctx.author.display_name}",
                    icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                await ctx.send(embed=embed2)
                await message.delete()
                return

            elif confirm.content == "reinstall":
                f = open("reinstall.txt")
                lines = f.read()
                f.close()
                f = open("reinstall_2.txt")
                lines2 = f.read()
                f.close()
                embed = discord.Embed(title="Reinstall Method",
                                      description=f"{lines}",
                                      colour=0x1ABC9C)
                embed2 = discord.Embed(description=f"{lines2}", color=0x1ABC9C)
                embed.set_author(
                    name=f"Command run by {ctx.author.display_name}",
                    icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                await ctx.send(embed=embed2)
                await message.delete()
                return

            elif confirm.content == "vanity":
                f = open("vanity.txt")
                lines = f.read()
                f.close()
                embed = discord.Embed(title="Vanity unban",
                                      description=f"{lines}",
                                      colour=0x1ABC9C)
                embed.set_author(
                    name=f"Command run by {ctx.author.display_name}",
                    icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                await message.delete()
                return

            else:
                return

        await message.edit(title="Cancelled", description=" ")


def setup(bot: commands.Bot):
    bot.add_cog(help1(bot))
