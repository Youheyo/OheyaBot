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

	# * COMMAND RELOADER
	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def reload_cog(self, ctx):

		await self.bot.change_presence(status=Status.dnd, activity=activity.CustomActivity(name = "Reloading!!!"))
		async with ctx.channel.typing():
			try:
				cog_list =[f for f in os.listdir(directory) if f.endswith('.py')]

				with tqdm(cog_list, unit="cog") as progress:
					msg = await ctx.send("Reloading commands...")
					x = 0
					for cog in progress:
						progress.set_description(f"Reloading {cog}")
						await self.bot.reload_extension(f'cogs.{cog[:-3]}')
						x += 1
						await msg.edit(content=f"Reload Progress: {(x/len(cog_list) * 100):.0f}%")
					await msg.edit(content=f"Commands Successfully Reloaded")
		
			except TimeoutError:
				await ctx.channel.send("ERROR: Time out. Commands failed to load")
		
		await self.bot.change_presence(status=Status.online, activity=activity.CustomActivity(name = "oh Good Morning!"))

	
	@commands.command(name='reset', hidden=True)
	@commands.is_owner()
	async def reset(self, ctx):
		print("Reconnecting to Discord")
		# await self.bot.close()
		exit(0)

async def setup(bot):
	await bot.add_cog(Moderator(bot))
