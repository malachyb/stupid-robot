import discord, asyncio


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


def help(command):
    try:
        return {"default": """```Commands list:
    hello:         greets the user who called it
    lenny:         sends a random lenny face
    cow:           sends a cow saying whatever message you follow the command with
    fortune:       sends a cow giving you a fortune
    crab:          sends a message with a crab doing a dance
    roll:          rolls a number of dice with any number of sides
    flip:          flips a coin
    emoji:         gives a random emoji
    zalgofy:       converts your message to zalgo text
    ascii:         converts your message to ASCII art
    animate:       creates an animation cycling through the characters of your message
    yoda:          translates your message into Yoda
    roast:         insults tagged user
    dog:           sends a picture of a dog
    cat:           sends a picture of a cat
    monkey:        sends a picture of a monkey
    giraffe:       sends a picture of a giraffe
    compatibility: Says how compatible you are with another user```""",
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
                "animate": "creates an animation cycling through the characters of your message. \n&animate [message]",
                "yoda":    "translates your message into Yoda. \n &yoda [message]",
                "roast":   "insults tagged user. \n&roast @[username]",
                "dog":     "sends a picture of a dog. \n&dog",
                "cat":     "sends a picture of a cat. \n&cat",
                "monkey":  "sends a picture of a monkey. \n&monkey",
                "giraffe": "sends a picture of a giraffe",
                "compatibility": "Says how compatible you are with another user. \n&compatibility @[user]"}[command]
    except KeyError:
        return "Error: Command not found"
