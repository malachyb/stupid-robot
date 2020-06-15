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
        await asyncio.sleep(0.25)



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
            command = command[1:]
            if command == "fortune":
                await channel.send(fortune())
            elif command == "lenny":
                await channel.send(lenny())
            elif command == "hello":
                await channel.send(hello(str(message.author).split('#')[0].capitalize()))
            elif command == "crab":
                await crab(channel)


client.run(TOKEN)
