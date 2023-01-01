import nextcord
from nextcord.ext import commands

import Information

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/hp ', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}!')


@client.command()
async def character(message, *, key):
    await Information.any_character_information(message, key)


@client.command()
async def professor(message, *, key):
    await Information.professors_character_information(message, key)


@client.command()
async def student(message, *, key):
    await Information.students_character_information(message, key)


@client.command()
async def spell(message, *, key):
    await Information.spell_information(message, key)


@client.command()
async def wand(message, *, key):
    await Information.wand_information(message, key)


@client.command()
async def broomstick(message, *, key):
    await Information.broomsticks_information(message, key)

client.run("MTA1Nzk5NTkyMzYxNzIyMjY5Ng.Gpj5rT.uaNy8GMoqbaX2LDjW-zXbIFQQykUnzFVIZVMjw")