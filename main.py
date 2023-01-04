import os

import nextcord
from nextcord import SlashOption
from nextcord.ext import commands
from typing import Optional

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
                                  "Novel Series", guild_ids=[1057997352926986260])
async def character(interaction: nextcord.Interaction, name):
    await Information.any_character_information(interaction, name)


@client.slash_command(description="Will give you information about any Professor teaching at Hogwarts in "
                                  "Harry Potter Novel Series", guild_ids=[1057997352926986260])
async def professor(message: nextcord.Interaction, name):
    await Information.professors_character_information(message, name)


@client.slash_command(description="Will give you information about any Student studying at Hogwarts in "
                                  "Harry Potter Novel Series", guild_ids=[1057997352926986260])
async def student(message: nextcord.Interaction, name):
    await Information.students_character_information(message, name)


@client.slash_command(description="Will give you information about any Spell used in "
                                  "Harry Potter Novel Series", guild_ids=[1057997352926986260])
async def spell(message: nextcord.Interaction, name):
    await Information.spell_information(message, name)


@client.slash_command(description="Will give you information about any Wand present in "
                                  "Harry Potter Novel Series", guild_ids=[1057997352926986260])
async def wand(message: nextcord.Interaction, owner):
    await Information.wand_information(message, owner)


@client.slash_command(description="Will give you information about any Broomstick present in "
                                  "Harry Potter Novel Series", guild_ids=[1057997352926986260])
async def broomstick(message: nextcord.Interaction, name):
    await Information.broomsticks_information(message, name)


@client.slash_command(description="Will give you information about any book related to Harry Potter",
                      guild_ids=[1057997352926986260])
async def book(message: nextcord.Interaction, id: Optional[int] = SlashOption(required=False)):
    if id is None:
        await Information.all_books(message)
    elif id:
        await Information.books_information(message, id)


client.run(TOKEN)
