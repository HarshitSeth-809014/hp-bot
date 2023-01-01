import nextcord
from nextcord.ext import commands

import Information

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.id}!')


@client.slash_command(description="Will give you information about any character present in Harry Potter "
                                  "Novel Series")
async def character(interaction: nextcord.Interaction, name):
    await Information.any_character_information(interaction, name)


@client.slash_command(description="Will give you information about any Professor teaching at Hogwarts in "
                                  "Harry Potter Novel Series")
async def professor(message: nextcord.Interaction, name):
    await Information.professors_character_information(message, name)


@client.slash_command(description="Will give you information about any Student studying at Hogwarts in "
                                  "Harry Potter Novel Series")
async def student(message: nextcord.Interaction, name):
    await Information.students_character_information(message, name)


@client.slash_command(description="Will give you information about any Spell used in "
                                  "Harry Potter Novel Series")
async def spell(message: nextcord.Interaction, name):
    await Information.spell_information(message, name)


@client.slash_command(description="Will give you information about any Wand present in "
                                  "Harry Potter Novel Series")
async def wand(message: nextcord.Interaction, name):
    await Information.wand_information(message, name)


@client.slash_command(description="Will give you information about any Broomstick present in "
                                  "Harry Potter Novel Series", guild_ids=[1057997352926986260])
async def broomstick(message: nextcord.Interaction, name):
    await Information.broomsticks_information(message, name)


client.run("MTA1Nzk5NTkyMzYxNzIyMjY5Ng.Gpj5rT.uaNy8GMoqbaX2LDjW-zXbIFQQykUnzFVIZVMjw")
