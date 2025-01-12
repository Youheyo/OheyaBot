from discord.ext import commands
import discord
import json

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		with open('config.json') as f:
			data = json.load(f)
			self.link = data['invite']

	@commands.command()
	async def echo(self, ctx, *text):
		'''Echoes back your message'''
		argument = ' '.join(text)
		await ctx.send(f'{argument}')

	@commands.command(name='eya')
	async def oheya(self, ctx):
		"""Says Hello"""
		await ctx.send(f"Hello!")

	@commands.command()
	async def invite(self, ctx):
		'''Get an Invite to the server'''
		embed = discord.Embed(
			title="Oh Hey Yo Invite",
			url = self.link,
			description = "Invite to the server",
			colour=discord.Colour.orange()
		)
		embed.set_thumbnail(url = "https://azurlane.netojuu.com/images/4/4a/ClevelandChibi.png")
		await ctx.send(embed=embed)


	@commands.command()
	async def ping(self, ctx):
		'''Checks the latency'''
		print(f"Pong! {round(self.bot.latency* 1000, 2)} ms")
		await ctx.send(f"Pong! {round(self.bot.latency* 1000, 2)} ms")

async def setup(bot):
	await bot.add_cog(General(bot))