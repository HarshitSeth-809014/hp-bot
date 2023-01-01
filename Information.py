import json

import discord
import requests
import nextcord

SPELL_API = json.loads(requests.get('https://hp-api.onrender.com/api/spells').text)
CHARACTERS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters').text)
STUDENTS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters/students').text)
PROFESSORS_API = json.loads(requests.get('https://hp-api.onrender.com/api/characters/staff').text)
with open('./data/broomsticks.json', 'r') as f:
    BROOMSTICK_API = json.load(f)


async def create_embed(api, message, check):
    for val in api:
        if val['name'].lower() == check.lower():
            embed = nextcord.Embed(title=val['name'])
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


async def wand_information(message, wand):
    await message.response.send_message(f'all {wand} information')


async def professors_character_information(message, professor):
    await create_embed(PROFESSORS_API, message, professor)


async def students_character_information(message, student):
    await create_embed(STUDENTS_API, message, student)


async def any_character_information(message, character):
    await create_embed(CHARACTERS_API, message, character)


async def spell_information(message, spell):
    for val in SPELL_API:
        if spell == val['name'].lower():
            await message.response_send_message(f'Spell: ```{val["name"]}```\nUse: ```{val["description"]}```')


async def broomsticks_information(message, broomstick):
    for val in BROOMSTICK_API:
        if val['name'].lower() == broomstick.lower():
            embed = discord.Embed(title=val['name'], description=val['description'])
            if val['image']:
                embed.set_image(url=val['image'])
            await message.response.send_message(embed=embed)
    await message.response.send_message('Broomstick not found!!! Try again.')
