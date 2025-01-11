from discord.ext import commands

class eya(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='eya', description='Say hello')
	async def oheya(self, ctx):
		"""Says Hello"""
		await ctx.send(f"Hello!")

async def setup(bot):
	await bot.add_cog(eya(bot))