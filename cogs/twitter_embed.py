"""
Replaces sent message to include vx and other related prefixes (idk what its called)

"""

import discord
from discord.ext import commands


class TwitFix(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(name = "fix",
					usage="ohfix [link]",
					description = "Adds in the prefix on twitter link")
	@commands.guild_only()
	@commands.has_permissions()
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def fix(self, ctx:commands.Context, message: str):
		'''Places the prefix vx on twitter links'''

		# print(message)
		# msg = message

		sites = ["https://", "twitter.com", "x.com"]

		if not message.startswith("https://"): return

		match message:
			case str() if "x.com" in message:
				msg = message.replace("x.com", "vxtwitter.com")
			case str() if "twitter.com" in message:
				msg = message.replace("twitter.com", "vxtwitter.com")

		await ctx.message.delete()
		await ctx.channel.send(f"{ctx.author.mention} sent {msg}")


async def setup(bot:commands.Bot):
	await bot.add_cog(TwitFix(bot))