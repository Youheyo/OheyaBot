from discord.ext import commands
import discord

class ping(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx):
		print(f"Pong! {round(self.bot.latency* 1000, 2)} ms")
		await ctx.send(f"Pong! {round(self.bot.latency* 1000, 2)} ms")

async def setup(bot):
	await bot.add_cog(ping(bot))
	