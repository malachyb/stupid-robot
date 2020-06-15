import discord, requests, asyncio, random
from subprocess import Popen, PIPE


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


def roll(size):
    return random.randint(1, size)


def flip():
    return random.choice(["heads", "tails"])
