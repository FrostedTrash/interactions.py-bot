from discord.ext import commands
import interactions


class Vorlage(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(...)
    async def test_command(self, ctx, ...):    

def setup(client):
    Vorlage(client)