import os
import asyncio
import json
import discord

from tqdm import tqdm
from discord.ext import commands


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
    cog_list = (file for file in os.listdir(directory + '/cogs') if file.endswith('.py'))
    with tqdm(cog_list, unit="cog") as cogs:
        cogs.write("Cog loading in progress...")
        for cog in cogs:
            cogs.set_description(f"Loading {cog}")
            await bot.load_extension(f'cogs.{cog[:-3]}')
        cogs.write("Cog loading finished!")

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