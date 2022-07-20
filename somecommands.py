from multiprocessing.sharedctypes import Value
import time

from discord.ext import commands # Again, we need this imported
import discord
import interactions
from requests import delete


class Somecommands(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
      name="ping",
      description="Shows the Bots Latency.",
    )
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms") # It's now self.bot.latency



    @interactions.extension_command(
      name="setstatus",
      description="Sets the Bots Apperance",
      options = [
        interactions.Option(
          name="activity",
          description="Set the bots activity",
          type=interactions.OptionType.STRING,
          required=True,
          ),
        interactions.Option(
          name="acttype",
          description="Set the activity Type.",
          type=interactions.OptionType.STRING,
          choices=[
            interactions.Choice(
              name = "GAME",
              value = "GAME",
            ),
            interactions.Choice(
              name="STREAMING",
              value="STREAMING",
            ),
          ],
        ),
      ],
    )
    async def setstatus(self, ctx: commands.Context, *, activity: str, acttype: str):
      #Bot Status
      if acttype == "GAME":
        activitytype = interactions.PresenceActivityType.GAME
      elif acttype == "STREAMING":
        activitytype = interactions.PresenceActivityType.STREAMING
      msg = await ctx.send("Noch in arbeit")
      time.sleep(5)
      await msg.delete()
      #await self.bot.change_presence(interactions.ClientPresence(activities=[interactions.PresenceActivity(name=activity, type=activitytype)]))
    
def setup(client):
    Somecommands(client)