import discord
from discord.ext import commands


class Testing(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(name = "testmemberjoin")
	@commands.is_owner()
	async def simulate_member_join(self, ctx:commands.Context):
		await ctx.send("Sending Test Member join")
		await self.bot.on_member_join(ctx.author)

async def setup(bot:commands.Bot):
	await bot.add_cog(Testing(bot))