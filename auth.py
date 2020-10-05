from database import DatabaseCommunicator
import time


async def check_command_permission(ctx, command):
    user_id = str(ctx.author.id)
    guild = str(ctx.guild.id)
    db = DatabaseCommunicator(guild)
    auth = await db.auth.find_one({"user_id": str(user_id), "access": command})
    return False if auth is None else True
