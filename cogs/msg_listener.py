import os
import json
import random

import discord
from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))

class msg_listener(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		with open(os.path.dirname(directory)+'/message_listener_actions.json','r', encoding='utf-8') as f:
			data = json.load(f)
			self.triggers = data["keyword_responses"]
			# print(self.triggers)
			# print(type(self.triggers))


	@commands.Cog.listener()
	@commands.guild_only()
	async def on_message(self, ctx):
		'''Sends a message or do action based on message content'''

		# NOTE:   Ensure bot doesn't respond to itself
		if ctx.author.bot:
			return

		for i, word_list in enumerate(self.triggers):
			for word in word_list['keyword']:
				if word in ctx.content.lower():
					response = word_list['response']
					print(response)
					await ctx.channel.send(response)

					emoji_id = word_list['reaction']
					print(emoji_id)
					emoji: discord.Emoji = ctx.guild.get_emoji(emoji_id)
					await ctx.add_reaction(word_list['reaction'])

					break

async def setup(bot):
	await bot.add_cog(msg_listener(bot))
