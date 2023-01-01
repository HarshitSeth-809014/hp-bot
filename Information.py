import json

import requests
import nextcord

SPELL_API = json.loads(requests.get('https://hp-api.onrender.com/api/spells').text)
CHARACTERS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters').text)
STUDENTS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters/students').text)
PROFESSORS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters/staff').text)


async def create_embed(api, message, check):
    for val in api:
        if val['name'].lower() == check:
            embed = nextcord.Embed(title=val['name'])
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
            if val['image']:
                embed.set_thumbnail(url=val['image'])

            await message.send(embed=embed)


async def wand_information(message, wand):
    await message.send(f'all {wand} information')


async def professors_character_information(message, professor):
    await create_embed(PROFESSORS_API, message, professor)


async def students_character_information(message, student):
    await create_embed(STUDENTS_API, message, student)


async def any_character_information(message, character):
    await create_embed(CHARACTERS_API, message, character)


async def spell_information(message, spell):
    for val in SPELL_API:
        if spell == val['name'].lower():
            await message.send(f'Spell: ```{val["name"]}```\nUse: ```{val["description"]}```')


async def broomsticks_information(message, broomstick):
    await message.send(f'all {broomstick} info')