# Work with Python 3.6
import discord

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

word_list = []
story_active = False

@client.event
async def on_message(message):
    global word_list, story_active
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!story help'):
        msg = 'How to use:\n!begin story:   Starts a story!\n!add <enter word(s) here>:   Adds new words to the story!\n!end story:   Ends the story!'
        await message.channel.send(msg)
    elif message.content.startswith('!begin story'):
        word_list = ['Once', 'upon', 'a', 'time,']
        msg = 'Let the story begin...'
        story_active = True
        await message.channel.send(msg)
    elif story_active and message.content.startswith('!add'):
        msg = message.content
        if msg.startswith('!add ') == False:
            msg = msg[:4] + ' ' + msg[4:]

        word_list.extend(msg.split(' ')[1:])
        msg = " ".join(word_list)
        await message.channel.send(msg)

    elif story_active and message.content.startswith('!end story'):
        msg = 'And that\'s the end of the story! This was what the story was about:'
        await message.channel.send(msg)
        msg = " ".join(word_list)
        story_active = False
        await message.channel.send(msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
