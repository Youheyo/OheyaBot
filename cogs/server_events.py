import os
import json;
import discord
from discord.ext import commands

directory = os.path.dirname(os.path.abspath(__file__))

class ServerEvent(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		with open(os.path.dirname(directory)+'/server_ids.json') as f:
			data = json.load(f)
			self.main_channel_id = data['main_channel']


	@commands.Cog.listener()
	async def on_member_join(self, ctx):
		main_channel: discord.channel  = self.bot.get_channel(self.main_channel_id)
		# await self.bot.fetch_user(151816823782899714).send(f"A member has joined! {ctx}")
		await main_channel.send(f"A member has joined!")
		await main_channel.send(f"Heyo it's {ctx.mention}!")

	@commands.Cog.listener()
	async def on_member_remove(self, ctx):
		main_channel: discord.channel  = self.bot.get_channel(self.main_channel_id)
		await main_channel.send(f"Man... {ctx} left...")


async def setup(bot:commands.Bot):
	await bot.add_cog(ServerEvent(bot))