"""
Moderator related commands

Commands:

prune	- Delete messages by specified amount Requires Manage_Messages permission. 

! Currently doesn't seem to be working
reload	- Reloads cogs

- - - - -

Listeners:

on_message - Checks for banned words. Deletes and pings the author afterwards


"""
import os
import time

from tqdm import tqdm
from sys import exit
from asyncio import TimeoutError
from discord.ext import commands
from discord import Status, activity


directory = os.path.dirname(os.path.abspath(__file__))

BANNED_WORDS = []

class Moderator(commands.Cog):
    
	def __init__(self, bot):
		self.bot = bot


	# * TEXT CHANNEL PRUNING
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def prune(self, ctx, num: int = 0):
		'''Delete messages up to a specified amount'''
		if(num < 1):
			await ctx.send("No messages were deleted")
			return
		deleted = await ctx.channel.purge(limit=num+1)
		print(f'{ctx.author} pruned {len(deleted)-1} messages in {ctx.channel}')
		await ctx.send(f'{len(deleted) -1} messages were deleted', delete_after=5 )


	# * PROFANITY CHECKER
	@commands.Cog.listener()
	async def on_message(self, ctx):
		if any(word in ctx.content.lower() for word in BANNED_WORDS):
			await ctx.delete()
			await ctx.channel.send(f"That's a no no word {ctx.author.mention}! 😩👉👈")

async def setup(bot):
	await bot.add_cog(Moderator(bot))
