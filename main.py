import os
from dotenv import load_dotenv
from commands import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    print("Ya boi is here")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    channel = message.channel
    command = message.content
    if command[0] == '&':
        async with channel.typing():
            command = command[1:].split()
            if command[0] == "fortune":
                await channel.send(fortune())
                return
            elif command[0] == "lenny":
                await channel.send(lenny())
                return
            elif command[0] == "hello":
                await channel.send(hello(str(message.author).split('#')[0].capitalize()))
                return
            elif command[0] == "crab":
                await crab(channel, client)
                return
            elif command[0] == "cow":
                await channel.send(cow(' '.join(command[1:])))
                return
            elif command[0] == "help":
                await channel.send(help(command[1] if len(command) > 1 else "default"))
                return
            elif command[0] == "roll":
                await channel.send(roll(*map(int, command[1:])))
                return
            elif command[0] == "flip":
                await channel.send(flip())
                return
            elif command[0] == "emoji":
                await channel.send(emoji(channel.guild))
                return
            elif command[0] == "zalgofy":
                try:
                    await channel.send(zalgofy(' '.join(command[1:])))
                except IndexError:
                    await channel.send("Need a message to zalgofy")
                return
            elif command[0] == "ascii":
                try:
                    await channel.send(ascii('+++'.join(command[1:])))
                except IndexError:
                    await channel.send("Need a message to turn into ASCII")
                return
            elif command[0] == "animate":
                try:
                    await animate(' '.join(command[1:]), channel, client)
                except IndexError:
                    await channel.send("Need a message to turn into ASCII")
                return
            await channel.send("Command not found, try &help for a list of available commands")


client.run(TOKEN)
