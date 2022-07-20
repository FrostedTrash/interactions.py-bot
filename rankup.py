from discord.ext import commands
import discord


class Vorlage(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    #bans a user with a reason
    @commands.command(name = "rankup")
    @commands.has_role(983975830868860958)
    async def rankup (ctx, member:discord.User=None):
        message = f"You have just been ranked up from {ctx.message.author}"
        await member.send(message)
        role = discord.utils.get(commands.get_guild(ctx.guild.id).roles, id = "921013889964068865")
        await member.add_roles(role)
        await ctx.channel.send(f"{member} has been ranked up!")
    

def setup(bot: commands.Bot):
    bot.add_cog(Vorlage(bot))