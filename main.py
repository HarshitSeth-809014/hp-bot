import os

import nextcord
from nextcord import SlashOption
from nextcord.ext import commands
from typing import Optional

import Help
import Information
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

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
async def wand(message: nextcord.Interaction, owner):
    await Information.wand_information(message, owner)


@client.slash_command(description="Will give you information about any Broomstick present in "
                                  "Harry Potter Novel Series")
async def broomstick(message: nextcord.Interaction, name):
    await Information.broomsticks_information(message, name)


@client.slash_command(description="Will give you information about any book related to Harry Potter")
async def book(message: nextcord.Interaction, id: int):
    await Information.books_information(message, id)


@client.slash_command(description="Name the command like "
                                  "'book', 'broomstick', 'character', 'professor', 'spell', 'student' and 'wand'")
async def help(message, command: str):
    await Help.all_help(message=message, com=command)


client.run(TOKEN)
