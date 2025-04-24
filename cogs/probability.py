from discord.ext import commands
import random


class Probability(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx, alias="flipcoin"):
        await ctx.reply("Heads" if random.randint(1, 2) == 1 else "Tails")

    @commands.command()
    async def choose(self, ctx, *text, alias="choice"):
        pass

async def setup(bot):
	await bot.add_cog(Probability(bot))