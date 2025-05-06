"""
Probability Related commands

Commands:
coinflip    -   flips a coin for heads or tails: 50/50
choose      -   Chooses randomly from options provided by user

"""

from discord.ext import commands
import random


class Probability(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx, alias="flipcoin"):
        '''Flip a coin'''
        await ctx.reply("Heads" if random.randint(1, 2) == 1 else "Tails")

    @commands.command()
    async def choose(self, ctx, *, text, alias="choice"):
        '''Randomly picks from at least 2 options'''
        choices = text.split('|')
        if(len(choices) < 2):
             await ctx.reply("Not enough choices. Please provide more e.g `ohchoose apple | orange | lemon`")
        else:
            await ctx.reply(random.choice(choices))


async def setup(bot):
	await bot.add_cog(Probability(bot))