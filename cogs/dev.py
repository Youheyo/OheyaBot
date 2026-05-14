import os
from tqdm import tqdm
import discord
from discord import Status, activity
from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))

class dev(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def reload_cog(self, ctx, cog):
		try:
			if cog.lower() == 'all':
				await self.reload_all_cogs(ctx)
				return
			elif cog.lower() == 'full':
				await self.full_reload(ctx)
				return
			else:
				await self.bot.reload_extension(f'cogs.{cog}')
		except (commands.ExtensionNotFound, commands.ExtensionNotLoaded) as e:
			await ctx.send(f"Error {e}: Please check if the command is loaded or correct", delete_after=5)
		except commands.ExtensionFailed:
			await ctx.send("Command failed to load.")
		else:
			await ctx.send(f"{cog} successfully reloaded", delete_after=5)

	# * COMMAND RELOADER
	@commands.command(name='reloadall', hidden=True)
	@commands.is_owner()
	async def reload_all_cogs(self, ctx):

		await self.bot.change_presence(status=Status.dnd, activity=activity.CustomActivity(name = "Reloading!!!"))
		async with ctx.channel.typing():
			cog_list =[f for f in os.listdir(directory) if f.endswith('.py')]

			print(" - - - - - ")
			with tqdm(cog_list, unit="cog") as progress:
					msg = await ctx.send("Reloading commands...")
					for count, cog in enumerate(progress, 1):
						try:
			
							progress.set_description(f"Reloading {cog}")
							await self.bot.reload_extension(f'cogs.{cog[:-3]}')
							await msg.edit(content=f"Reload Progress: {(count/len(cog_list) * 100):.0f}%")
	
						except TimeoutError:
							await ctx.channel.send("ERROR: Time out. Commands failed to load")
						except commands.ExtensionNotLoaded as e:
							await ctx.channel.send(f"ERROR {e}: A command hasn't been loaded yet. Please do a full reload through `ohfullreload` or add it manually through `ohloadcog [command]`")
							not_loaded_count += 1
							continue
						else:
							print(" - - - - - ")
							await msg.edit(content=f"{count-not_loaded_count} Commands Successfully Reloaded")
						finally:
							await self.bot.change_presence(status=Status.online, activity=activity.CustomActivity(name = "oh Good Morning! | use ohhelp for list of commands"))

	
	@commands.command(name='fullreload', hidden=True)
	@commands.is_owner()
	async def full_reload(self, ctx):
		await self.bot.change_presence(status=Status.dnd, activity=activity.CustomActivity(name = "Attempting to full reload.."))
		try:
			cog_list =[f for f in os.listdir(directory) if f.endswith('.py')]
			print(" - - - - - ")
			msg = await ctx.send("Unloading commands...")

			with tqdm(cog_list, unit="cog") as progress:
					x = 0
					for cog in progress:
						progress.set_description(f"Unloading {cog}")
						try:
							await self.bot.unload_extension(f'cogs.{cog[:-3]}')
						except commands.ExtensionNotLoaded:
							continue
						x += 1
						await msg.edit(content=f"Unload Progress: {(x/len(cog_list) * 100):.0f}%")
					print(" - - - - - ")
					await msg.edit(content="Commands Successfully Unloaded")

			with tqdm(cog_list, unit="cog") as progress:
					x = 0
					for cog in progress:
						progress.set_description(f"Loading {cog}")
						await self.bot.load_extension(f'cogs.{cog[:-3]}')
						x += 1
						await msg.edit(content=f"Loading Progress: {(x/len(cog_list) * 100):.0f}%")
					print(" - - - - - ")
					await msg.edit(content="Commands Successfully Loaded")
		
		except TimeoutError:
			await ctx.channel.send("ERROR: Time out. Commands failed to load")
		finally:
			await self.bot.change_presence(status=Status.online, activity=activity.CustomActivity(name = "oh Good Morning! | use ohhelp for list of commands"))

	@commands.command(name='loadcog', hidden=True)
	@commands.is_owner()
	async def load_cog(self, ctx, cog):
		try:
			await self.bot.load_extension(f'cogs.{cog}')
		except commands.ExtensionNotFound:
			await ctx.send("Command not found. Are you sure it's the right name?", delete_after=5)
		except commands.ExtensionAlreadyLoaded:
			await ctx.send("Command already loaded!", delete_after=5)
		else:
			await ctx.send(f"{cog} loaded!", delete_after=5)

	@commands.command(name='unloadcog', hidden=True)
	@commands.is_owner()
	async def unload_cog(self, ctx, cog):

		# ! Ensure dev cog doesn't get unloaded outside of full reload
		if(cog.lower() == 'dev'):
			await ctx.send("You cannot unload dev", delete_after=5)
			return
		try:
			await self.bot.unload_extension(f'cogs.{cog}')
		except commands.ExtensionNotFound:
			await ctx.send("Command not found. Are you sure it's the right name?", delete_after=5)
		except commands.ExtensionNotLoaded:
			await ctx.send("Cannot unload a command not loaded in.", delete_after=5)
		else:
			await ctx.send(f"{cog} unloaded!", delete_after=5)




	@commands.command(name='reset', hidden=True)
	@commands.is_owner()
	async def reset(self, ctx):
		print("Reconnecting to Discord")
		# await self.bot.close()
		exit(0)


async def setup(bot:commands.Bot):
	await bot.add_cog(dev(bot))