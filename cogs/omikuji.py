import discord
from discord.ext import commands
import r
import json
import random

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="おみくじ")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def omi1(self, ctx):
        print("test")

def setup(bot):
    bot.add_cog(test(bot))
