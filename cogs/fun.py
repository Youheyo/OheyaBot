"""
Fun commands anyone on the server can use

Commands:


"""

WORDS_OF_WISDOM = ["Baller", "KYS! NOW *thunder* I mean that with a 100%. With a 1000%", "Uninstall your gacha games. It'd be healthy :)"]

import random
from discord.ext import commands
import discord

class Fun(commands.Cog):


	@commands.command()
	async def ball(self, ctx, alias="8"):
		'''Gives out a random message'''
		random.seed()
		await ctx.send(f'{random.choice(WORDS_OF_WISDOM)}')

async def setup(bot):
	await bot.add_cog(Fun(bot))
