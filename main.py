# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random

import json

with open('config.json') as f:
    data = json.load(f)
    token = data["token"]
    prefix = data["prefix"]


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = "A 4Fun bot currently being developed into discord.py"

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    print(f"Pong!")
    await ctx.send("Pong!")

@bot.command()
async def echo(ctx, *text):
    argument = ' '.join(text)
    await ctx.send(f'{argument}')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def prune(ctx, num: int):
    if(num < 1):
        await ctx.send("No messages were deleted")
        return
    deleted = await ctx.channel.purge(limit=num+1)
    await ctx.send(f'{len(deleted) -1} messages were deleted', delete_after=5 )

@bot.command()
async def eya(ctx):
    await ctx.send(f"Hello!")

bot.run(token)
