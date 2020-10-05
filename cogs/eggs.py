import discord
from discord.ext import commands
import emoji
import auth


class Eggs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def whoami(self, ctx):
        france = emoji.emojize(":France:")
        await ctx.send(f"24601! {france}")

    @commands.command()
    async def isitlit(self, ctx):
        fire = emoji.emojize(":fire:")
        await ctx.send(f"Always! {fire}")


def setup(client):
    client.add_cog(Eggs(client))
