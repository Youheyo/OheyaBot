from discord.ext import commands
import discord

class invite(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		import json
		with open('config.json') as f:
			data = json.load(f)
			self.link = data['invite']

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

async def setup(bot):
	await bot.add_cog(invite(bot))