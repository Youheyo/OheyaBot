"""
General use commands anyone on the server can use

Commands:

Echo 	- Echoes back message
eya  	- Replies with Hello
invite 	- Sends an embed with the invite link
ping	- Replies with 'Pong' and the latency

"""
import json
from discord.ext import commands
import discord

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		with open('config.json') as f:
			data = json.load(f)
			self.link = data['invite']

	@commands.command()
	async def echo(self, ctx, *text, alias="Echo"):
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
		await ctx.send(self.link)


	@commands.command()
	async def ping(self, ctx):
		'''Checks the latency'''
		print(f"Pong! {round(self.bot.latency* 1000, 2)} ms")
		await ctx.send(f"Pong! {round(self.bot.latency* 1000, 2)} ms")

async def setup(bot):
	await bot.add_cog(General(bot))