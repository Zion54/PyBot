import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Pydoc has entered the chat uwu')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('.pydoc'):
        await msg.channel.send('Test 1')

client.run('NzU4MTA3NjM3MDY0NjYzMDQz.X2qIwQ.KeVefjnsfNEilXaPKMlzmj4t-CY')

