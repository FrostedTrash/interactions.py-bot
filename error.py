from discord.ext import commands
import discord

class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title="Cooldown Error", description=f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.", colour=0xE74C3C)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Permission Error", description="You are missing the required permissions to run this command!", colour=0xE74C3C)
        elif isinstance(error, commands.UserInputError):
            embed = discord.Embed(title="Imput Error", description="Something about your input was wrong, please check your input and try again!", colour=0xE74C3C)
        elif isinstance(error, commands.MissingRole):
            embed = discord.Embed(title="Permission Error", description="No, No, Don't touch me there! Permission Error!", colour=0xE74C3C)
        else:
            embed = discord.Embed(title= "General Error", description="I really dont know why this error happened", colour=0xE74C3C)

        #await ctx.send(message, delete_after=5)
        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete(delay=5)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))