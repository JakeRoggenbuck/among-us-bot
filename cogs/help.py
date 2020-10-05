import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def amongushelp(self, ctx):
        embed = discord.Embed(title="Help", color=0x00D3FF)
        embed.add_field(name="Add permission", value=".add @name perm", inline=True)
        embed.add_field(
            name="Remove permission", value=".remove @name perm", inline=True
        )
        embed.add_field(name="Roll Dice", value=".roll ndn (e.g. 1d4)", inline=True)
        embed.add_field(
            name="Rename channel to code", value=".code code (e.g. YTNMAQ)", inline=True
        )
        embed.add_field(name="Check permisson", value=".check @name perm", inline=True)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
