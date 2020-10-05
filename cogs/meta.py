import discord
from discord.ext import commands
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


def setup(client):
    client.add_cog(Sudo(client))
