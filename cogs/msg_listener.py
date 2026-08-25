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

		# NOTE: Ensure bot doesn't respond to itself
		if ctx.author.bot:
			return

		for i, word_list in enumerate(self.triggers):
			print("Checking group:",i,len(word_list['keyword']), "words", word_list)
			for word in word_list['keyword']:
				print("Sample word")
				# print(f"Checking if {word} is detected in {ctx.content}")
				# FIX: For loop does not work. It only reads the first word then nothing else. 
				#try:
				# 	response = word_list['response']
				# 	print(response)
				# 	await ctx.channel.send(response)
				#
				# 	emoji_id = word_list['reaction']
				# 	emoji = ctx.guild.get_emoji(emoji_id)
				#
				# 	# * Check if emoji is not any of the list. Default to emoji_id
				# 	if not isinstance(emoji, (str, discord.Emoji, discord.Reaction)):
				# 		emoji = emoji_id
				# 	print(emoji)
				# 	await ctx.add_reaction(emoji)
				#
				# except Exception as e:
				# 	await ctx.channel.send("An Error Occurred", delete_after=3)
				# 	print(f"Error: {e}")
				
async def setup(bot):
	await bot.add_cog(msg_listener(bot))
