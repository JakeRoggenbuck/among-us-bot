import discord
from discord.ext import commands
import emoji
import auth


class Base(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.command()
    async def ping(self, ctx):
        ping_pong = emoji.emojize(":ping_pong:")
        await ctx.send(f"Pong! {self.client.latency*1000:2.3f} ms {ping_pong}")


def setup(client):
    client.add_cog(Base(client))
