from database import DatabaseCommunicator
import time


async def check_command_permission(ctx, command):
    # Get ids of the roles the user has
    ids = [x.id for x in ctx.author.roles]
    # Gets the users personal id
    user_id = str(ctx.author.id)
    # Adds personal id to list
    ids.append(user_id)

    # Sets up guild db
    guild = str(ctx.guild.id)
    db = DatabaseCommunicator(guild)
    # Checks if any id has permissions
    for _id in ids:
        auth = await db.auth.find_one({"user_id": str(_id), "access": command})
        # If auth returns a value, user has permissions via the _id role
        if auth is not None:
            return True
    return False
