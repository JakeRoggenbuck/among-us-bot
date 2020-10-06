import discord
from discord.ext import commands
import auth
import regex


class ChannelName(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def code(self, ctx, new_name):
        authorized = await auth.check_command_permission(ctx, "code")
        if authorized:
            pattern = regex.compile("[A-Z]{6}")
            # Check if new_name.upper() matches pattern
            name = pattern.search(new_name.upper())
            if name is not None:
                # Get vc name
                voice_channel_name = ctx.author.voice.channel
                # Change vc name to new name
                await voice_channel_name.edit(name=name.group(0))
            else:
                await ctx.send(f"name not a valid code")
        else:
            await ctx.send(f"permission denied")


def setup(client):
    client.add_cog(ChannelName(client))
