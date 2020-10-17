import discord
from discord.ext import commands
import emoji
import auth
import motor.motor_asyncio as motor


class WildMagic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def magic(self, ctx, number):
        number = number.zfill(4)
        client = motor.AsyncIOMotorClient()
        db = client["wild_magic"]
        collection = db["collection"]
        roll = await collection.find_one({"roll": int(number)})
        if roll is not None:
            await ctx.send(f"{number}: {roll['text']}")

def setup(client):
    client.add_cog(WildMagic(client))
