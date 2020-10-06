import discord
from discord.ext import commands
import subprocess
import emoji
import auth


class Sudo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx, extention):
        authorized = await auth.check_command_permission(ctx, "load")
        if authorized:
            self.client.load_extension(f"cogs.{extention}")
            await ctx.send(f"{extention} loaded!")
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def unload(self, ctx, extention):
        authorized = await auth.check_command_permission(ctx, "unload")
        if authorized:
            self.client.unload_extension(f"cogs.{extention}")
            await ctx.send(f"{extention} unloaded!")
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def reload(self, ctx, extention):
        authorized = await auth.check_command_permission(ctx, "reload")
        if authorized:
            self.client.unload_extension(f"cogs.{extention}")
            self.client.load_extension(f"cogs.{extention}")
            await ctx.send(f"{extention} reloaded!")
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def ping(self, ctx):
        ping_pong = emoji.emojize(":ping_pong:")
        await ctx.send(f"Pong! {self.client.latency*1000:2.3f} ms {ping_pong}")

    @commands.command()
    async def version(self, ctx):
        version = 1.0
        commit = subprocess.check_output('git log --format="%H" -n 1', shell=True).decode("utf-8").strip("\n")
        await ctx.send(f"Bot {version} at {commit[0:6]}")


def setup(client):
    client.add_cog(Sudo(client))
