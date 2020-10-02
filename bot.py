from mongofastlogger.logger import Logger
import discord.ext.commands as commands
import motor.motor_asyncio as motor
import discord
from utils import Config
import os


client = commands.Bot(command_prefix=".")


@client.command()
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")


@client.command()
async def unload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")


@client.command()
async def reload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    client.load_extension(f"cogs.{extention}")


for extention in os.listdir('./cogs'):
    if extention.endswith('.py'):
        client.load_extension(f"cogs.{extention[:-3]}")

config = Config('config.yml')
client.run(config.client_secret)
