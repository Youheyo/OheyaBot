"""
Replaces sent message to include vx and other related prefixes (idk what its called)

"""

import discord
from discord.ext import commands


class PrefixLink(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(name = "fix",
					usage="ohfix [link]",
					description = "Adds in the prefix on links for discord embedding"
					)
	@commands.guild_only()
	@commands.has_permissions()
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def fix(self, ctx:commands.Context, message: str):
		'''Places the prefix on respective links. Works for Twitter, Reddit, instagram, and Tiktok'''
		# print(message)
		# msg = message

		# * Check if message is a link
		if not message.startswith("https://"): return

		match message:
			case str() if "x.com" in message:
				msg = message.replace("x.com", "fixvx.com")
			case str() if "twitter.com" in message:
				msg = message.replace("twitter.com", "vxtwitter.com")

			case str() if "reddit.com" in message:
				msg = message.replace("reddit.com", "rxddit.com")

			case str() if "instagram.com" in message:
				msg = message.replace("instagram.com", "dinstagram.com")

			case str () if "tiktok.com" in message:
				msg = message.replace("tiktok.com", "vxtiktok.com")

		await ctx.message.delete()
		await ctx.channel.send(f"{ctx.author.mention} sent {msg}")


async def setup(bot:commands.Bot):
	await bot.add_cog(PrefixLink(bot))