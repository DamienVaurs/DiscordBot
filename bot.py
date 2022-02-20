import discord
import os; os.system("pip3 install [package]")



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


a = 2
my_secret = os.environ['TOKEN']
client.run(my_secret)
