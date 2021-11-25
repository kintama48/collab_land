import json
import os
import sys
from random import randint

import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


def has_roles(context):
    roles = [role.name for role in context.message.author.roles]
    if "Admin" in roles:
        return True
    return False


class Claim(commands.Cog, name="claim"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join", description=f"Join collab.land")
    async def join(self, context):
        embed = discord.Embed(color=0x00aacc, description="**Connect Your Account\n**"
                                                                     f"To connect your wallet/account please [Click here]({config['redirect_link']}).")
        await context.author.send(embed=embed)
#         await context.reply(embed=discord.Embed(color=0x109ab5, description="**Please check your DMs :)**"))



def setup(bot):
    bot.add_cog(Claim(bot))
