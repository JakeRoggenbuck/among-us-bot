import discord
import discord.ext.commands as commands
import emoji


class Base(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.command()
    async def ping(self, ctx):
        ping_pong = emoji.emojize(":ping_pong:")
        await ctx.send(f"Pong! {ping_pong}")


def setup(client):
    client.add_cog(Base(client))
