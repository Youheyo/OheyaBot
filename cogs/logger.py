import time
from discord.ext import commands


class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # * TERMINAL LOGGING
    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f'{ctx.author} triggered {ctx.command} in {ctx.channel}')
        ctx.start_time = ctx.time.perf_counter()


    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f'{ctx.author} | Finished {ctx.command} in {ctx.channel}')
        # duration = (time.perf_counter() - ctx.start_time)
        # print(f'{ctx.author} triggered {ctx.command} in {ctx.channel} | Took {duration}')


async def setup(bot):
    await bot.add_cog(Logger(bot))