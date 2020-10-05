import discord.ext.commands as commands
import discord
from utils import Config
import os


client = commands.Bot(command_prefix=".")

for extention in os.listdir('./cogs'):
    if extention.endswith('.py'):
        client.load_extension(f"cogs.{extention[:-3]}")

config = Config('config.yml')
client.run(config.client_secret)
