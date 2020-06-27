import discord, requests, random, re, faker, datetime
from subprocess import Popen, PIPE


def my_ord(inp):
    return int(''.join(map(str, [ord(i) for i in inp])))


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


def compatibility(user1: discord.User, user2: discord.User):
    random.seed(my_ord(user1.name + user2.name))
    return f"{user1.mention} compatibility with {user2.mention} is {random.randint(0, 100)}%"


def cool(user: discord.User):
    random.seed(my_ord(user.name))
    return f"{user.mention} is {random.randint(0, 100)}% cool"


def space():
    early_date = datetime.date(year=2000, month=1, day=1)
    date = faker.Faker().date_between(start_date=early_date, end_date="now")
    return requests.get(f"https://api.nasa.gov/planetary/apod?api_key=6F14k5aw1jvo6DaWr2xTFec57S6oYSgL3gvEv3Qa&hd=true&date={date}").json()["hdurl"]
