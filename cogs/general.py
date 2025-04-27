"""
General use commands anyone on the server can use

Commands:

Echo 	- Echoes back message
eya  	- Replies with Hello
invite 	- Sends an embed with the invite link
ping	- Replies with 'Pong' and the latency

- - - - -

Listeners:

on_message - Detects when a user has a certain string of words
			- Tags
				- KMS and related
"""

import os
import json
from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		with open(os.path.dirname(directory)+'/config.json') as f:
			data = json.load(f)
			self.link = data['invite']

	@commands.command()
	async def echo(self, ctx, *text, alias="Echo"):
		'''Echoes back your message'''
		argument = ' '.join(text)
		await ctx.send(f'{argument}')

	@commands.command(name='eya', hidden=True)
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

	@commands.Cog.listener()
	async def on_message(self, ctx):

		'''Sends a message depending on the message content'''

		if(ctx.author.bot):
			return

		keyword = ['kms', 'kill myself', 'kill my self' ]
		# file = discord.File("./uploads/neverkys.mp4", filename="neverkys.mp4")
		if any(word in ctx.content.lower() for word in keyword):
			# await ctx.channel.send(file = file)
			async with ctx.channel.typing():
				await ctx.channel.send("https://cdn.discordapp.com/attachments/905278576482476042/1365220101456134184/neverkys.mp4")
		
		keyword = ['kys', 'kill yourself', 'kill your self']
		if any(word in ctx.content.lower() for word in keyword ):
			async with ctx.channel.typing():
				await ctx.delete()
				await ctx.channel.send(f"{ctx.author.mention} says")
				await ctx.channel.send(f"https://tenor.com/view/keep-your-self-safe-gif-26048046")

async def setup(bot):
	await bot.add_cog(General(bot))