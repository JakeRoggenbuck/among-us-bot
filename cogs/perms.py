import discord
from discord.ext import commands
from database import DatabaseCommunicator
import auth
import utils


class Perms(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, mention, perm):
        user_id = utils.clean_mention(mention)
        authorized = await auth.check_command_permission(ctx, "add")
        if authorized:
            guild = str(ctx.guild.id)
            db = DatabaseCommunicator(guild)
            await db.auth.find_one_and_update({"user_id": user_id},{"$push": {"access": perm}}, upsert=True)
            await ctx.send(f"{mention} added to {perm}")
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def remove(self, ctx, mention, perm):
        user_id = utils.clean_mention(mention)
        authorized = await auth.check_command_permission(ctx, "remove")
        if authorized:
            guild = str(ctx.guild.id)
            db = DatabaseCommunicator(guild)
            await db.auth.find_one_and_update({"user_id": user_id}, { "$pull": { "access": { "$in": [perm] }} })
            await ctx.send(f"{mention} removed from {perm}")
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def check(self, ctx, mention, perm):
        user_id = utils.clean_mention(mention)
        authorized = await auth.check_command_permission(ctx, "check")
        if authorized:
            guild = str(ctx.guild.id)
            db = DatabaseCommunicator(guild)
            has_perm = await db.auth.find_one({"user_id": user_id, "access": perm})
            if has_perm is not None:
                await ctx.send(f"User has {perm}")
            else:
                await ctx.send(f"User does not have {perm}")
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def make_admin(self, ctx, mention):
        user_id = utils.clean_mention(mention)
        authorized = await auth.check_command_permission(ctx, "make_admin")
        if authorized:
            guild = str(ctx.guild.id)
            db = DatabaseCommunicator(guild)
            await db.auth.find_one_and_update({"user_id": user_id},{"$push": {"access": { "$each": ["add", "remove", "check", "load", "unload", "reload", "make_admin", "code"]}}}, upsert=True)
            await ctx.send(f"{mention} added as admin")
        else:
            await ctx.send(f"permission denied")


def setup(client):
    client.add_cog(Perms(client))
