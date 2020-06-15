import os, discord, requests, asyncio
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


async def crab(channel: discord.TextChannel):
    crabs = ["(/)(;,,;)(/)", "(\\\\)(;,,;)(\\\\)"] * 10
    await channel.send("crab")
    message = 0
    async for tmp in channel.history(limit=10):
        if tmp.author == client.user:
            message = tmp
            break
    for i in crabs:
        await message.edit(content=i)
        await asyncio.sleep(0.1)


def cow(phrase):
    return "```" + str(Popen(["cowsay", phrase], stdout=PIPE).communicate()[0], "utf-8") + "```"


def help(command):
    try:
        return {"default": """```Commands list:
    hello:   greets the user who called it
    lenny:   sends a random lenny face
    cow:     sends a cow saying whatever message you follow the command with
    fortune: sends a cow giving you a fortune
    crab:    sends a message with a crab doing a dance```""",
                "hello":   "hello: greets the user who called it",
                "lenny":   "lenny: sends a random lenny face",
                "cow":     "cow: sends a cow saying whatever message you follow the command with",
                "fortune": "fortune: sends a cow giving you a fortune",
                "crab":    "crab: sends a message with a crab doing a dance"}[command]
    except KeyError:
        return "Error: Command not found"


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
                await crab(channel)
                return
            elif command[0] == "cow":
                await channel.send(cow(' '.join(command[1:])))
                return
            elif command[0] == "help":
                await channel.send(help(command[1] if len(command) > 1 else "default"))
                return


client.run(TOKEN)
