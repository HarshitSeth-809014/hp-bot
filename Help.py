import nextcord


async def all_help(message: nextcord.Interaction, com: str):
    if com == 'book':
        await books_help(message=message)
    elif com == 'broomstick':
        await broomsticks_help(message=message)
    elif com == 'character':
        await character_help(message=message)
    elif com == 'professor':
        await professor_help(message=message)
    elif com == 'spell':
        await spell_help(message=message)
    elif com == 'wand':
        await wand_help(message=message)
    elif com == 'student':
        await student_help(message=message)


async def books_help(message: nextcord.Interaction):
    embed = nextcord.Embed(title="Books", description="You must refer to a particular book by id.\n"
                                                      "Use: ```/book id:<id>```",
                           colour=nextcord.Color.from_rgb(242, 94, 61))
    embed.add_field(name="Harry Potter and the Sorcerer's Stone", value="ID: 1")
    embed.add_field(name="Harry Potter and the chamber of secrets", value="ID: 2")
    embed.add_field(name="Harry Potter and the Prisoner of Azkaban", value="ID: 3")
    embed.add_field(name="Harry Potter and the Goblet of Fire", value="ID: 4")
    embed.add_field(name="Harry Potter and the Order of the Phoenix", value="ID: 5")
    embed.add_field(name="Harry Potter and the Half-Blood Prince", value="ID: 6")
    embed.add_field(name="Harry Potter and the Deathly Hallows", value="ID: 7")
    embed.add_field(name="Harry Potter and the Cursed Child", value="ID: 8")

    await message.response.send_message(embed=embed)


async def broomsticks_help(message: nextcord.Interaction):
    await message.response.send_message(embed=nextcord.Embed(title="You must refer to a particular broomstick by "
                                                                   "name",
                                                             description="Use: ```/broomstick name:<name>```"))


async def character_help(message: nextcord.Interaction):
    await message.response.send_message(embed=nextcord.Embed(title="You must refer to a particular character by "
                                                                   "name",
                                                             description="Use: ```/character name:<name>```"))


async def professor_help(message: nextcord.Interaction):
    await message.response.send_message(embed=nextcord.Embed(title="You must refer to a particular professor by "
                                                                   "name",
                                                             description="Use: ```/professor name:<name>```"))


async def spell_help(message: nextcord.Interaction):
    await message.response.send_message(embed=nextcord.Embed(title="You must refer to a particular spell by "
                                                                   "name",
                                                             description="Use: ```/spell name:<name>```"))


async def student_help(message: nextcord.Interaction):
    await message.response.send_message(embed=nextcord.Embed(title="You must refer to a particular student by "
                                                                   "name",
                                                             description="Use: ```/student name:<name>```"))


async def wand_help(message: nextcord.Interaction):
    await message.response.send_message(embed=nextcord.Embed(title="You must refer to a particular wand by "
                                                                   "name",
                                                             description="Use: ```/wand owner:<name>```"))
