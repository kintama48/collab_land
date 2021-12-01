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
        embed = discord.Embed(color=0x00ACF0, description="**Connect Your Account\n**"
                                                                     f"To connect your wallet/account please [Click here]({config['redirect_link']}).")
        try:
            await context.author.send(embed=embed)
            await context.send(content=f"{context.author.mention} Please check dm.")
        except:
            await context.send(content=f"{context.author.mention} Failed to send DM. Please enable DM `User Settigs > Privacy & Safety > Allow direct messages from server members.` and try again.")



def setup(bot):
    bot.add_cog(Claim(bot))
