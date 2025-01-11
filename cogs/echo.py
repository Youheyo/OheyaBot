import discord
from discord.ext import commands

class echo(commands.Cog):
	
	def __init__(self, bot):
			self.bot = bot
			
	@commands.command()
	async def echo(self, ctx, *text):
		argument = ' '.join(text)
		await ctx.send(f'{argument}')

async def setup(bot):
	await bot.add_cog(echo(bot))