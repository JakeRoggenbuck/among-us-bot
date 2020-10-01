from mongofastlogger.logger import Logger
import discord.ext.commands as commands
import motor.motor_asyncio as motor
import discord
import random
import emoji
import yaml


client = commands.Bot(command_prefix=".")


class Config:
    def __init__(self, path: str):
        self.path = path
        self.config = self.get_config()
        self.client_secret = self.config["client_secret"]

    def get_config(self):
        config_file = open(self.path)
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        return config


@client.event
async def on_ready():
    print("Ready")


@client.command()
async def ping(ctx):
    ping_emoji = emoji.emojize(":ping_pong:")
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms {ping_emoji} ")


@client.command(aliases=["r"])
async def roll(ctx, question):
    count, num = question.split("d")
    total = 0
    for x in range(int(count)):
        my_roll = random.randint(1, int(num))
        total += my_roll
    await ctx.send(f"{total}")


config = Config('config.yml')
client.run(config.client_secret)
