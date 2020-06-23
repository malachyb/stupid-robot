import discord, requests, random, re
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


def roll(size=6, count=1):
    return sum((random.randint(1, size) for i in range(count)))


def flip():
    return random.choice(["heads", "tails"])


def emoji(server):
    return random.choice(server.emojis)


def roast(user: discord.User):
    req = requests.get("https://evilinsult.com/generate_insult.php?lang=en")
    insult = req.text
    return user.mention + " " + insult


def image(tag):
    req = requests.get(f"https://api.flickr.com/services/feeds/photos_public.gne?format=json&tags={tag}")
    req = eval(req.text.replace("jsonFlickrFeed(", "")[:-1])
    req = random.choice(req["items"])["description"]
    req = re.findall('src=\".*\"', req)[0].split('"')[1].replace("\\/", '/')
    return req
