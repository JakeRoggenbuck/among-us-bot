import discord
from discord.ext import commands
import random
import emoji

import utils


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx, user_roll, verbose="no"):
        # Checks for user entered verbosity
        if verbose == "verbose" or verbose == "-v":
            verbose = True
            individual_rolls = []
        else:
            verbose = False
        # Splits ndn into ["n", "n"] and assigns to dice_num and dice_value
        dice_num, dice_value = user_roll.split("d")
        total_roll = 0
        # Rolls a value for range of dice_num
        for roll in range(int(dice_num)):
            # Rolls a random value with min of one and max of dice_value
            current_roll = random.randint(1, int(dice_value))
            total_roll += current_roll
            # Add verbose output to message
            if verbose:
                individual_rolls.append(f"- {current_roll}\n")
        message = f"Rolled {total_roll}"
        if verbose:
            message += utils.generate_multi_line_highlight(individual_rolls)
        await ctx.send(message)


def setup(client):
    client.add_cog(Example(client))
