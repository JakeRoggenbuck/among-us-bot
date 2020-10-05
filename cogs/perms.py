import discord
import discord.ext.commands as commands
from database import DatabaseCommunicator
import auth


class Perms(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, user_id, perm):
        authorized = await auth.check_command_permission(ctx, "add")
        if authorized:
            guild = str(ctx.guild.id)
            db = DatabaseCommunicator(guild)
            await db.auth.find_one_and_update({"user_id": user_id},{"$push": {"access": perm}}, upsert=True)
            await ctx.send(f"{user_id} added to {perm}")
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def remove(self, ctx, user_id, perm):
        authorized = await auth.check_command_permission(ctx, "remove")
        if authorized:
            guild = str(ctx.guild.id)
            db = DatabaseCommunicator(guild)
            await db.auth.find_one_and_update({"user_id": user_id}, { "$pull": { "access": { "$in": [perm] }} })
            await ctx.send(f"{user_id} removed to {perm}")
        else:
            await ctx.send(f"permission denied")


def setup(client):
    client.add_cog(Perms(client))
