import discord
from memes import process_msg, name_of_file

TOKEN = 'MTA2Njk4MzE4NzYxNzY5Mzc1Ng.GQqF_3.zagO715ajgWMviSRwIy3ljYzuJOt9-b0Fkt1do'

client = discord.Client(intents=discord.Intents.all())

@client.event   
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if str(message.channel) == 'memes' and str(message.author) != 'Meme Bot#1917' and str(message.content)[0] == '>':
        print(f'{message.author} said {message.content} on #memes')
        
        p = process_msg(message)

        if p[0]:
            await message.channel.send(p[0])
        elif p[1]:
            with open(name_of_file, 'rb') as m:
                await message.channel.send(file=discord.File(m))

client.run(TOKEN)