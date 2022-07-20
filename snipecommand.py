from discord.ext import commands # Again, we need this imported
import discord


class SnipeCommand(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
      self.last_msg = message

    @commands.command(name="snipe")
    async def snipe(self, ctx:commands.Context):
      #Snipe command
      if not self.last_msg: #on_message_delete hasn't been triggered since the bot started
        await ctx.send("There is no message to snipe!")
        return

      author = self.last_msg.author
      content = self.last_msg.content

      embed = discord.Embed(title=f"Message from {author}", description=content)
      await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(SnipeCommand(bot))