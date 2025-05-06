"""
Terminal Logging purposes
    Actually need to make better logging

Listeners:
on_command              -   Outputs to terminal time command was made
on_command_completion   -   Outputs to terminal time command was completed
                            - Kinda wanted to make it track how long it took to finish a command
on_command_error        -   Outputs to terminal when a command errors
                            - Haven't tested. Unknown if it works


"""


from datetime import datetime
from discord.ext import commands


class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # * TERMINAL LOGGING
    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f'{datetime.now().strftime("%H:%M:%S")} : {ctx.author} triggered {ctx.command} in #{ctx.channel}')


    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f'{datetime.now().strftime("%H:%M:%S")} : {ctx.author} | Finished {ctx.command} in #{ctx.channel}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f"{datetime.now().strftime("%H:%M:%S")} : Command {ctx.command} failed to run: Error {error}")


async def setup(bot):
    await bot.add_cog(Logger(bot))