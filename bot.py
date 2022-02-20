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


client.run('NDQ0NDYwMDg0NTUxMjIxMjQ4.WvV9tQ.3zxA6Ld089gi6mNYc56-Zw8ouxQ')
