import discord, requests, asyncio, random
from subprocess import Popen, PIPE
from zalgo_text import zalgo


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


async def crab(channel: discord.TextChannel, client):
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
    crab:    sends a message with a crab doing a dance
    roll:    rolls a number of dice with any number of sides
    flip:    flips a coin
    emoji:   gives a random emoji
    zalgofy: converts your message to zalgo text
    ascii:   converts your message to ASCII art
    animate: creates an animation cycling through the characters of your message```""",
                "hello":   "hello: greets the user who called it. \n&hello",
                "lenny":   "lenny: sends a random lenny face. \n&lenny",
                "cow":     "cow: sends a cow saying whatever message you follow the command with. \n&cow [message]",
                "fortune": "fortune: sends a cow giving you a fortune. \n&fortune",
                "crab":    "crab: sends a message with a crab doing a dance. \n&crab",
                "roll":    "rolls a number of dice with any number of sides. \n&roll [optional(sides)] [optional(count)]",
                "flip":    "flips a coin. \n&flip",
                "emoji":   "gives a random emoji. \n&emoji",
                "zalgofy": "converts your message to zalgo text. \n&zalgofy [text]",
                "ascii":   "converts your message to ASCII art. \n&ascii [text]",
                "animate": "creates an animation cycling through the characters of your message. \n&animate [message]"}[command]
    except KeyError:
        return "Error: Command not found"


def roll(size=6, count=1):
    return sum((random.randint(1, size) for i in range(count)))


def flip():
    return random.choice(["heads", "tails"])


def emoji(server):
    return random.choice(server.emojis)


def zalgofy(text):
    return zalgo.zalgo().zalgofy(text)


def ascii(text):
    req = requests.get(f"http://artii.herokuapp.com/make?text={text}")
    return "```" + req.text + "```"


async def animate(text, channel, client):
    await channel.send(text)
    async for tmp in channel.history(limit=10):
        if tmp.author == client.user:
            message = tmp
            break
    for char in text:
        await message.edit( content="```" +requests.get(f"http://artii.herokuapp.com/make?text={char}").text + "```")
        await asyncio.sleep(0.1)
