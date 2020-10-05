import discord
from discord.ext import commands
from database import DatabaseCommunicator
import auth
import utils


class Perms(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def generic_query_command(self, *args):
        """Run command in mongodb and check for permission by discord user

        e.g. ".add @name code" (Adding the role "code" to the user @name)
        """
        # ctx is context
        ctx = args[0]
        # perm is what command is being run e.g. add
        perm = args[1]

        # message is what's displayed when success
        message = args[2]

        # query is the search query for find_one_and_update
        query = args[3]
        # action is what mongodb is being told to update
        action = args[4]

        # upsert is the optional argument of weather to upsert or not
        if len(args) == 6:
            upsert = args[5]
        else:
            upsert = False

        authorized = await auth.check_command_permission(ctx, perm)
        if authorized:
            db = DatabaseCommunicator(str(ctx.guild.id))
            await db.auth.find_one_and_update(query, action, upsert=upsert)
            await ctx.send(message)
        else:
            await ctx.send(f"permission denied")

    @commands.command()
    async def add(self, ctx, mention, role):
        user_id = utils.clean_mention(mention)
        await self.generic_query_command(
            ctx,
            "add",
            f"{mention} added to {role}",
            {"user_id": user_id},
            {"$push": {"access": role}},
            True,
        )

    @commands.command()
    async def remove(self, ctx, mention, role):
        user_id = utils.clean_mention(mention)
        await self.generic_query_command(
            ctx,
            "remove",
            f"{mention} removed from {role}",
            {"user_id": user_id},
            {"$pull": {"access": {"$in": [role]}}},
        )

    @commands.command()
    async def make_admin(self, ctx, mention):
        user_id = utils.clean_mention(mention)
        await self.generic_query_command(
            ctx,
            "make_admin",
            f"{mention} was made admin",
            {"user_id": user_id},
            {
                "$push": {
                    "access": {
                        "$each": [
                            "add",
                            "remove",
                            "check",
                            "load",
                            "unload",
                            "reload",
                            "make_admin",
                            "code",
                        ]
                    }
                }
            },
            True,
        )

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


def setup(client):
    client.add_cog(Perms(client))
