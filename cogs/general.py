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
from datetime import datetime
import discord
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

def msg_trigger_handler(trigger_check, rand100=-1):
	text = f'{datetime.now().strftime("%H:%M:%S")} : {trigger_check} - Trigger Word Detected'
	if(rand100 > 0):
		text += f" - Rolled a {rand100}"
	print(text)
	# print(f"{datetime.now().strftime("%H:%M:%S")} : {trigger_check} - Trigger Word Detected - {rand100}")


async def setup(bot):
	await bot.add_cog(General(bot))
