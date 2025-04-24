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
from os import listdir
from discord.ext import commands
from discord import Status, activity

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
		await ctx.send("Reloading commands...")
		print("-----\nReloading commands")
		# bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name="oh Good Morning!"))
		await self.bot.change_presence(status=Status.dnd, activity=activity.CustomActivity(name = "Reloading!!!"))
		x = 0
		for cog in listdir('./cogs'):
			if cog.endswith('.py'):
				print(f"Loading in {cog}")
				await self.bot.reload_extension(f'cogs.{cog[:-3]}')
				x += 1
		print (f"{x} Commands Reloaded")
		await self.bot.change_presence(status=Status.online, activity=activity.CustomActivity(name = "oh Good Morning!"))
		await ctx.send(f"Commands Reloaded")

	# ! Not working as of now
	# @commands.command()
	# @commands.is_owner()
	# async def shutdown(self, ctx):
	# 	print("Shutting Down")
	# 	await ctx.Client.close()

async def setup(bot):
	await bot.add_cog(Moderator(bot))
