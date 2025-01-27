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
import datetime


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

	@commands.command(hidden=True)
	async def invite(self, ctx):
		'''Get an Invite to the server'''
		await ctx.send(self.link)


	@commands.command()
	async def ping(self, ctx):
		'''Checks the latency'''
		print(f"Pong! {round(self.bot.latency* 1000, 2)} ms")
		await ctx.send(f"Pong! {round(self.bot.latency* 1000, 2)} ms")

	@commands.command()
	async def epoch(self, ctx, *text):
		'''Converts time set into local time'''
		joined = ' '.join(text)
		print(joined)
		partition = joined.partition("|")
		print(partition[0])
		separator = 0
		# for x in text:
			# print(x)
			# if x.content == '|':
			# 	print("Separator found")
			# 	break
			# title = title + " " + x
			# separator += 1
		# title = newtext.partition("|")[0]

		# * DATETIME FORMAT
		# *	  0      1    2    3      4        5       6           7
		# * YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, MILISECOND, NANOSECOND

		# * EXPECTED USER FORMAT
		# * MONTH, DAY, HOUR, MINUTE
		# print(datetime.datetime.now())

		currDate = datetime.datetime.now()
		

		print("Title: " + title)	

async def setup(bot):
	await bot.add_cog(General(bot))