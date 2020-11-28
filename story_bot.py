# Work with Python 3.6
import discord
import os

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()
path = "data.txt"
word_list = []

def file_is_empty():
    return os.path.getsize(path) == 0

def clear_file():
    global path
    #clear file
    file = open("data.txt", "w").close()

def write_to_file(data):
    global path
    file = open(path, "w")
    try:
        file.write(data)
    finally:
        file.close()

def append_to_file(data):
    global path
    file = open(path, "a")
    try:
        file.write(data)
    finally:
        file.close()

def read_file():
    global path
    file = open(path, "r")
    try:
        return file.read()
    finally:
        file.close()

@client.event
async def on_message(message):
    global word_list
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!story help'):
        msg = 'How to use:\n!begin story:   Starts a story!\n!add <enter word(s) here>:   Adds new words to the story!\n!end story:   Ends the story!'
        await message.channel.send(msg)

    elif message.content.startswith('!begin story'):
        clear_file()
        word_list = ['Once', 'upon', 'a', 'time,']
        msg = 'Let the story begin...'
        await message.channel.send(msg)

        msg = " ".join(word_list)
        write_to_file(msg)

    elif message.content.startswith('!add'):
        #if story has not started
        if (file_is_empty()):
            await message.channel.send("The story has not begun!")
        else:
            msg = message.content
            if msg.startswith('!add ') == False:
                msg = msg[:4] + ' ' + msg[4:]

            word_list = msg.split(' ')[1:]
            msg = " ".join(word_list)
            append_to_file(" " + msg)
            data = read_file()
            await message.channel.send(data)

    elif message.content.startswith('!end story'):
        #if story has not started
        if (file_is_empty()):
            await message.channel.send("The story has not begun!")
        else:
            msg = 'And that\'s the end of the story! This was what the story was about:'
            await message.channel.send(msg)
            data = read_file()
            await message.channel.send("\n\n" + data)
            clear_file()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    clear_file()

client.run(TOKEN)
