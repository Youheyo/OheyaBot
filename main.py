import os
import asyncio
import discord
from discord.ext import commands

import json

directory = os.path.dirname(os.path.abspath(__file__))

with open(directory + "/config.json") as f:
    data = json.load(f)
    token = data["token"]
    prefix = data["prefix"]

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = "A 4Fun bot currently being developed into discord.py\nThe bot uses 'oh' as the prefix"

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), description=description, intents=intents)

async def load():
    for cog in os.listdir(directory + '/cogs'):
        if cog.endswith('.py'):
            print(f"Loading in {cog}")
            await bot.load_extension(f'cogs.{cog[:-3]}')

async def main():
    async with bot:
        await load()
        await bot.start(token)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name="oh Good Morning!"))

asyncio.run(main())