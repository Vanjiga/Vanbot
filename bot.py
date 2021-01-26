import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
 
        await message.channel.send('Hello!')


#remember to take out token before publishing so you dont get nae naed

client.run('')