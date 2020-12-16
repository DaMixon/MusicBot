import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import os
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("Dobra jestem gotowy".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("%Witam"):
        await message.channel.send("Siemka ;)")
        
client.run(os.getenv('Nzg4NzA3OTk2ODE3NTU1NDU2.X9nbjw.7ESqUHTMvansMUUyo0KInr7WQNk'))


