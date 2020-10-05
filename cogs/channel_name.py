import discord
import discord.ext.commands as commands
import auth


class ChannelName(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def code(self, ctx, new_name):
        authorized = await auth.check_command_permission(ctx, "code")
        if authorized:
            voice_channel_name = ctx.author.voice.channel
            await voice_channel_name.edit(name=new_name)
        else:
            await ctx.send(f"permission denied")


def setup(client):
    client.add_cog(ChannelName(client))
