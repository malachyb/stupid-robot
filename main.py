import os, discord, requests
from dotenv import load_dotenv
from subprocess import Popen, PIPE

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


def fortune():
    ret_str = Popen(["fortune"], stdout=PIPE).communicate()[0]
    while "Q:" in str(ret_str, "utf-8") or "--" in str(ret_str, "utf-8"):
        ret_str = Popen(["fortune"], stdout=PIPE).communicate()[0]
    return "```" + str(Popen(["cowsay", ret_str], stdout=PIPE).communicate()[0], "utf-8") + "```"


def lenny():
    req = requests.get("https://api.lenny.today/v1/random").json()[0]
    return req["face"]


@client.event
async def on_ready():
    print("Ya boi is here")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
    message = message.content
    if message[0] != '&':
        return
    command = message[1:]
    if command == "fortune":
        await channel.send(fortune())
    elif command == "lenny":
        await channel.send(lenny())

client.run(TOKEN)
