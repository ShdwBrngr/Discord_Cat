# Import libraries
import os
import discord
import requests
from dotenv import load_dotenv
import random

# Load API keys from .env file
load_dotenv()
cat_API = os.getenv("CAT_API_KEY")
discord_token = os.getenv("DISCORD_TOKEN")

# Function to fetch a meme (from r/memes if no subreddit is given)
def get_meme(subreddit="memes"):
    response = requests.get(f'https://meme-api.com/gimme/{subreddit}')
    data = response.json()
    title = data.get("title")
    url = data.get("url")
    return title, url if data else None

# Function to fetch a random cat image using TheCatAPI
def get_cat_meme():
    headers = {"x-api-key": cat_API}
    response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
    data = response.json()[0]
    url = data.get("url")
    return url if data else None

cat_images = {
    "common" : [
        "https://i.pinimg.com/736x/10/bc/bd/10bcbdc51fdacda178fbf70267e19251.jpg",
        "https://i.pinimg.com/736x/50/96/4d/50964dd2dde0828247aaf26f697f93aa.jpg",
        "https://i.pinimg.com/736x/90/54/c9/9054c9d1c125fe8d48b457694d325003.jpg",
        "https://i.pinimg.com/736x/9e/b7/a3/9eb7a3152c18b9ec987ca250d28eb92e.jpg",
        "https://i.pinimg.com/736x/85/61/98/8561985bacec7121a94c572257b4b6ca.jpg",
        "https://i.pinimg.com/736x/66/0a/5c/660a5ca662400c7214850a00c6b721c6.jpg",
        "https://i.pinimg.com/736x/19/08/77/190877aeeef85934b9f81d2f66498cba.jpg",
        "https://i.pinimg.com/736x/b5/7e/a2/b57ea27a8a99395a6ae844ca77d18f60.jpg",
        "https://i.pinimg.com/736x/e6/89/47/e689476d68157a3b33961489db179a81.jpg",
        "https://i.pinimg.com/736x/6a/85/94/6a859415a67633a28e5e9b968ca9ee79.jpg"
    ],
    "rare" : [
        "https://i.pinimg.com/736x/69/d4/f5/69d4f553a801270cc080e78402855353.jpg",
        "https://i.pinimg.com/736x/90/68/d3/9068d39a1cc4173c33a69bd11a127fab.jpg",
        "https://i.pinimg.com/736x/16/ca/b1/16cab153397fc070d5369635ba891e8d.jpg",
        "https://i.pinimg.com/736x/8e/47/3e/8e473ed665ed5fe89a8b65cb8e50c5ca.jpg",
        "https://i.pinimg.com/736x/e4/4e/7e/e44e7e3509cde14078b955ed758299e5.jpg",
        "https://i.pinimg.com/736x/0a/12/68/0a12680b50ae5496a9575fb9cfa0e651.jpg",
        "https://i.pinimg.com/736x/87/e4/a6/87e4a652ee8e9d915ec82634184dcb6a.jpg",
        "https://i.pinimg.com/736x/7d/74/16/7d7416b4820df975d753ff31da0b9909.jpg",
        "https://i.pinimg.com/736x/0a/aa/07/0aaa074e5d590f6597c482563355e120.jpg"
    ],
    "epic" : [
        "https://i.pinimg.com/736x/0e/ee/9b/0eee9bfaf9217cacbc7aa387b6f07bb9.jpg",
        "https://i.pinimg.com/736x/f7/3f/30/f73f30cd53a02c785530584193bc5bb0.jpg",
        "https://i.pinimg.com/736x/cc/3d/20/cc3d2009161463f26b21db544ef2e2be.jpg",
        "https://i.pinimg.com/736x/b1/86/21/b1862191bd2085ca4a88e4be7b6087f3.jpg",
        "https://i.pinimg.com/736x/7d/51/44/7d5144ea0d55a3853dd6ff1d54aca19c.jpg",
        "https://i.pinimg.com/736x/5c/46/6d/5c466d998a807e0ee243ac852da5946a.jpg",
        "https://i.pinimg.com/736x/ef/74/7b/ef747b0c96bc123a7362d4b09cd186fe.jpg",
        "https://i.pinimg.com/736x/81/a6/b9/81a6b913da0f3942af7cb3fe6f72fd85.jpg",
        "https://i.pinimg.com/736x/6d/4a/02/6d4a022b29ce165692672be0d35ec1df.jpg",
        "https://i.pinimg.com/736x/4c/6c/ed/4c6ced1f236d4440b547b4a109e6caf9.jpg"
    ]
}

def cat_gacha():
    rarity = random.choices(["common", "rare", "epic"],
                           weights = [80, 15, 5])[0]
    url = random.choice(cat_images[rarity])
    return rarity, url

# Bot client class
class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="with cats!"))
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        # Ignore the bot's own messages
        if message.author == self.user:
            return

        content = message.content.lower()

        # 📖 Help command
        if content.startswith('$help'):
            help_text = """
            **🐾 CatBot Commands**
            `$meme` - Get a meme from r/memes
            `$imagefrom [subreddit]` - Get an image from a specific subreddit
            `$cat` - Get a random cat picture
            `$pull` - Cat Gacha pull
            (Soon: `$collection` for cat collection!, $craft for crafting cat pics)
            """
            await message.channel.send(help_text)

        # 🖼 Meme command (default subreddit)
        elif content.startswith('$meme'):
            title, url = get_meme()
            if title and url:
                embed = discord.Embed(title=f"From r/memes\n{title}")
                embed.set_image(url=url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Oops! Couldn't fetch a meme.")

        # 📷 Reddit image command with subreddit argument
        elif content.startswith('$imagefrom'):
            parts = content.split()
            subreddit = parts[1] if len(parts) > 1 else "memes"
            title, url = get_meme(subreddit)
            if title and url:
                embed = discord.Embed(title=f"From r/{subreddit}\n{title}")
                embed.set_image(url=url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(f"Couldn't fetch an image from r/{subreddit}")

        # 🐱 Cat pic command
        elif content.startswith('$cat'):
            url = get_cat_meme()
            if url:
                embed = discord.Embed(title="Here's a cat pic!")
                embed.set_image(url=url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Oops! Couldn't fetch a cat pic.")
        
        elif content.startswith("$pull"):
            rarity, url = cat_gacha()
            if rarity == "epic":
                color = discord.Color.gold()
            elif rarity == "rare":
                color = discord.Color.blue()
            else:
                color = discord.Color.light_gray()
            embed = discord.Embed(title=f"You pulled a {rarity} cat!",
                                  color=color)
            embed.set_image(url=url)
            await message.channel.send(embed=embed)

# Discord requires this to read message contents
intents = discord.Intents.default()
intents.message_content = True

# Run the bot
client = MyClient(intents=intents)
client.run(discord_token)
