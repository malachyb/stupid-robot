import os, discord, requests
from dotenv import load_dotenv
from subprocess import Popen, PIPE

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


def fortune():
    ret_str = Popen(["fortune"], stdout=PIPE).communicate()[0]
    while "Q:" in str(ret_str, "utf-8") or "--" in str(ret_str, "utf-8"):
        ret_str = Popen(["fortune"], stdout=PIPE).communicate()[0]
    return "```" + str(Popen(["cowsay", ret_str], stdout=PIPE).communicate()[0], "utf-8") + "```"


def lenny():
    req = requests.get("https://api.lenny.today/v1/random")
    req = req.json()[0]
    return req["face"]


def hello(name):
    return f"Hello {name}"


@client.event
async def on_ready():
    print("Ya boi is here")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
    command = message.content
    if command[0] == '&':
        command = command[1:]
        if command == "fortune":
            await channel.send(fortune())
        elif command == "lenny":
            await channel.send(lenny())
        elif command == "hello":
            await channel.send(hello(str(message.author).split('#')[0].capitalize()))


client.run(TOKEN)
