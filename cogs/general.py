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
import random
import discord
from datetime import datetime
from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		with open(os.path.dirname(directory)+'/config.json') as f:
			data = json.load(f)
			self.link = data['invite']
		with open(os.path.dirname(directory)+'/server_ids.json') as f:
			data = json.load(f)
			self.member_ids = list(data['member_id'].items())


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
	@commands.guild_only()
	async def on_message(self, ctx):

		'''Sends a message depending on the message content'''

		if(ctx.author.bot):
			return

		trigger_check: bool = False

		keyword = ['kms', 'kill myself', 'kill my self' ]
		# file = discord.File("./uploads/neverkys.mp4", filename="neverkys.mp4")
		if any(word in ctx.content.lower() for word in keyword):
			# await ctx.channel.send(file = file)
			async with ctx.channel.typing():
				trigger_check = True
				helpful_links = ["https://media.discordapp.net/attachments/805871223903879249/1367776359862243421/image.png?ex=6815d080&is=68147f00&hm=7991c557672b552bd3aade9ab7ef77f5a71a35ed5da158c2d8b9a7dc0115030d&=&format=webp&quality=lossless&width=903&height=896","https://cdn.discordapp.com/attachments/905278576482476042/1365220101456134184/neverkys.mp4"]
				await ctx.reply(random.choice(helpful_links))
		
		keyword = ['kys', 'kill yourself', 'kill your self']
		if any(word in ctx.content.lower() for word in keyword ):
			async with ctx.channel.typing():
				trigger_check = True
				await ctx.delete()
				await ctx.channel.send(f"{ctx.author.mention} says")
				await ctx.channel.send(f"https://tenor.com/view/keep-your-self-safe-gif-26048046")

		keyword = ['tom', 'tom com', 'tom.com', 'tomcom']
		if any(word in ctx.content.lower() for word in keyword ):
			try:
				id = await self.bot.fetch_user(self.member_ids[0][1])

				await ctx.add_reaction("🍅")

				print(f"{datetime.now().strftime("%H:%M:%S")} Tom Word Detected - {ctx.jump_url}")
				await id.send(f"Tom Mentioned in {ctx.jump_url}")
			except discord.NotFound:
				print(f"{id} cannot be found")
			except discord.HTTPException:
				print("Tom Sender failed to fetch user")

		if(trigger_check): print(f"{datetime.now().strftime("%H:%M:%S")} Trigger Word Detected")


async def setup(bot):
	await bot.add_cog(General(bot))
