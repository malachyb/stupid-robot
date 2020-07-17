import discord, requests, asyncio
from subprocess import Popen, PIPE
from zalgo_text import zalgo


def cow(phrase):
    return "```" + str(Popen(["cowsay", phrase], stdout=PIPE).communicate()[0], "utf-8") + "```"


def gnu(phrase):
    return "```" + str(Popen(["cowsay", "-f", "gnu", phrase], stdout=PIPE).communicate()[0], "utf-8") + "```"


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


def yoda(message):
    req = requests.get(f"https://api.funtranslations.com/translate/yoda.json?text={message}").json()
    return req["contents"]["translated"]

