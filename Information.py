import json

import requests
import nextcord

SPELL_API = json.loads(requests.get('https://hp-api.onrender.com/api/spells').text)
CHARACTERS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters').text)
STUDENTS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters/students').text)
PROFESSORS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters/staff').text)
with open('./data/broomsticks.json', 'r') as f:
    BROOMSTICK_API = json.load(f)
with open('./data/wands_by_name.json', 'r') as f:
    WANDS_NAME_API = json.load(f)
with open('./data/books.json', 'r') as f:
    BOOKS_API = json.load(f)


async def create_embed(api, message: nextcord.Interaction, check: str):
    for val in api:
        if val['name'].lower() == check.lower():
            embed = nextcord.Embed(title=val['name'], colour=nextcord.Color.from_rgb(242, 94, 61))
            if val['image']:
                embed.set_image(url=val['image'])
            if val['house']:
                embed.add_field(name="House:", value=val['house'], inline=True)
            if val['actor']:
                embed.add_field(name="Role played by:", value=val['actor'], inline=True)
            if val['alive']:
                embed.add_field(name="Alive:", value=val['alive'], inline=True)
            if val['dateOfBirth']:
                embed.add_field(name="Date Of Birth:", value=val['dateOfBirth'], inline=True)
            if val['wizard']:
                embed.add_field(name="Is wizard:", value=val['wizard'], inline=True)
            if val['ancestry']:
                embed.add_field(name="Ancestry:", value=val['ancestry'], inline=True)
            embed.add_field(name="Student at Hogwarts:", value=val['hogwartsStudent'], inline=True)
            embed.add_field(name="Professor at Hogwarts:", value=val['hogwartsStaff'], inline=True)
            if val['gender']:
                embed.add_field(name="Gender", value=val['gender'], inline=True)

            await message.response.send_message(embed=embed)
    await message.response.send_message("Name not found!!! Try Again")


async def wand_information(message: nextcord.Interaction, wand: str):
    for val in WANDS_NAME_API:
        if val['owner'].lower() == wand.lower():
            embed = nextcord.Embed(title=f"{val['owner']}'s wand", colour=nextcord.Color.from_rgb(242, 94, 61))
            if val['note']:
                embed.description = val['note']
            if val['wood']:
                embed.add_field(name="Wood", value=val['wood'])
            if val['core']:
                embed.add_field(name="Core", value=val['core'])
            if val['length']:
                embed.add_field(name="Length", value=val['length'])
            if val['flexibility']:
                embed.add_field(name="Flexibility", value=val['flexibility'])
            if val['image']:
                embed.set_image(url=val['image'])
            await message.response.send_message(embed=embed)
    await message.response.send_message("Wand not found!!! Try again.")


async def professors_character_information(message, professor):
    await create_embed(PROFESSORS_API, message, professor)


async def students_character_information(message, student):
    await create_embed(STUDENTS_API, message, student)


async def any_character_information(message, character):
    await create_embed(CHARACTERS_API, message, character)


async def spell_information(message, spell):
    for val in SPELL_API:
        if spell == val['name'].lower():
            await message.response.send_message(embed=nextcord.Embed(title=val['name'], description=val['description'],
                                                                     colour=nextcord.Color.from_rgb(242, 94, 61)))
    await message.response.send_message('Spell not found!!! Try again.')


async def broomsticks_information(message: nextcord.Interaction, broomstick):
    for val in BROOMSTICK_API:
        if val['name'].lower() == broomstick.lower():
            embed = nextcord.Embed(title=val['name'], description=val['description'],
                                   colour=nextcord.Color.from_rgb(242, 94, 61))
            if val['image']:
                embed.set_image(url=val['image'])
            await message.response.send_message(embed=embed)
    await message.response.send_message('Broomstick not found!!! Try again.')


async def books_information(message: nextcord.Interaction, id_book):
    for val in BOOKS_API:
        if id_book == val['id']:
            embed = nextcord.Embed(title=val['title'], description=val['description'],
                                   colour=nextcord.Color.from_rgb(242, 94, 61))
            embed.add_field(name="Release Date:", value=val['releaseDay'])
            embed.add_field(name="Author:", value=val['author'])

            await message.response.send_message(embed=embed)
