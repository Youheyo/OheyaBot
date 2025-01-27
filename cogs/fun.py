"""
Fun commands anyone on the server can use

Commands:

ball - Sends back a random line

"""

WORDS_OF_WISDOM = ["Baller", "KYS! NOW *thunder* I mean that with a 100%. With a 1000%", "Uninstall your gacha games", "It's a fine day to go jungling", "Sleepy time", "Lucky! Gamble away", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "Flower"]

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
