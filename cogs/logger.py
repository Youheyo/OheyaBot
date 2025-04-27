import time
from discord.ext import commands


class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # * TERMINAL LOGGING
    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f'{ctx.author} triggered {ctx.command} in {ctx.channel}')


    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f'{ctx.author} | Finished {ctx.command} in {ctx.channel}')

    # @commands.Cog.listener()
    # async def on_error(self, ctx, error):
    #     print(f"Command {ctx.command} failed to run: Error {error}")


async def setup(bot):
    await bot.add_cog(Logger(bot))