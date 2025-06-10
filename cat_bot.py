# Import libraries
import os # To access system files
import discord # For everything discord related
import requests # For requesting from servers
from dotenv import load_dotenv # For storing private files
import random # For the gacha mechanics

# Load API keys from .env file
load_dotenv() # Loads environment variables from a .env file into the OS environment (e.g., API keys, tokens)
cat_API = os.getenv("CAT_API_KEY") # Get an environment variable
discord_token = os.getenv("DISCORD_TOKEN") # Get an environment variable

# Function to fetch a meme (from r/memes if no subreddit is given)
def get_meme(subreddit="memes"):
    """
    Fetches a meme from the specified subreddit using the Meme API.
    Args:
        subreddit (str): The subreddit to fetch the meme from. Defaults to "memes".
    Returns:
        tuple: A tuple containing the title and URL of the meme, or (None, None) if not found.
    """
    response = requests.get(f'https://meme-api.com/gimme/{subreddit}') # Uses requests to get data from a server
    data = response.json() # Returns the JSON encoded content from the response
    title = data.get("title") # Gets the title from the JSON
    url = data.get("url") # Gets the URL form the JSON
    return (title, url) if data else (None, None) # Only return values if both title and url are present

# Function to fetch a random cat image using TheCatAPI
def get_cat_meme():
    """
    Fetches a cat image using the Cat API.
    Args:
        None
    Returns:
        str: The URL of the cat image, or None if not found.
    """
    headers = {"x-api-key": cat_API}
    response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers) # Uses requests to get data from a server
    data = response.json()[0] # Get the first (and only) result from the returned JSON list
    url = data.get("url") # Gets the URL form the JSON
    return url if data else None # Returns url if there's a valid data, None if there's not

# A dictionary that contains images of cats for the gacha system
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

# Function to pull a random cat image (gacha)
def cat_gacha():
    """
    Pulls a random cat image from the cat pool and returns its rarity and URL.
    Args:
        None
    Returns:
        tuple: A tuple containing the rarity of the cat image and its URL.
    """
    rarity = random.choices(["common", "rare", "epic"],
                           weights = [80, 15, 5])[0] # Randomly selects a rarity based on given weights: 80% common, 15% rare, 5% epic
    url = random.choice(cat_images[rarity]) # Fetches a url from the cat pool
    return rarity, url

# Bot client class
class MyClient(discord.Client):
    # Bot status (Playing with cats!)
    async def on_ready(self):
        """
        Called when the bot has successfully connected to Discord.
        Sets the bot's presence and prints a confirmation message.
        Args:
            None
        Returns:
            None
        """
        await self.change_presence(activity=discord.Game(name="with cats!")) 
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        """
        Called when a message is sent in a channel the bot has access to.
        Args:
            message (discord.Message): The message object containing the content and author.
        Returns:
            None
        """
        # Ignore the bot's own messages
        if message.author == self.user:
            return
        content = message.content.lower()
        # Help command
        if content.startswith('$help'): # Help command that explains all available bot commands
            help_text = """
            **Cat Bot 🐾 Commands**
            `$meme` - Get a meme from r/memes
            `$imagefrom [subreddit]` - Get an image from a specific subreddit
            `$cat` - Get a random cat picture
            `$pull` - Cat Gacha pull
            (Soon: `$collection` for cat collection!, $craft for crafting cat pics)
            """
            await message.channel.send(help_text)

        # Meme command (default subreddit)
        elif content.startswith('$meme'):
            title, url = get_meme() # Calls the get meme function
            try:
                embed = discord.Embed(title=f"From r/memes\n{title}") # Embeds a text and the image itself
                embed.set_image(url=url)
                await message.channel.send(embed=embed) # Sends the meme
            except Exception as e:
                await message.channel.send("Oops! Couldn't fetch a meme.") # Error
                print(f"Error fetching meme: {e}")

        # Reddit image post command with subreddit argument
        elif content.startswith('$imagefrom'):
            parts = content.split() # Splits the message into words (e.g., ['$imagefrom', 'cats'])
            subreddit = parts[1] if len(parts) > 1 else "memes" # Fetches the subreddit given by the user
            title, url = get_meme(subreddit) # Calls the get meme function with a specified subreddit
            try: # Same process as the $meme command
                embed = discord.Embed(title=f"From r/{subreddit}\n{title}")
                embed.set_image(url=url)
                await message.channel.send(embed=embed)
            except Exception as e:
                await message.channel.send(f"Oops, Couldn't fetch an image from r/{subreddit}")
                print(f"Error fetching meme: {e}")

        # Cat pic command
        elif content.startswith('$cat'):
            url = get_cat_meme() # Calls the get cat meme function
            try: # Same process as $meme
                embed = discord.Embed(title="Here's a cat pic!")
                embed.set_image(url=url)
                await message.channel.send(embed=embed)
            except Exception as e:
                await message.channel.send("Oops! Couldn't fetch a cat pic.")
                print(f"Error fetching meme: {e}")
        
        # Cat gacha pull command
        elif content.startswith("$pull"):
            rarity, url = cat_gacha() # Calls the cat gacha function
            if rarity == "epic": # Sets embed color: gold for epic, blue for rare, gray for common
                color = discord.Color.gold()
            elif rarity == "rare":
                color = discord.Color.blue()
            else:
                color = discord.Color.light_gray()
            rarity_message = f"a {rarity}" if rarity != "epic" else f"an {rarity}"
            embed = discord.Embed(title=f"You pulled {rarity_message} cat!",
                                  color=color)
            embed.set_image(url=url)
            await message.channel.send(embed=embed)

# Discord requires this to read message contents
intents = discord.Intents.default()
intents.message_content = True

# Run the bot
client = MyClient(intents=intents)
client.run(discord_token)
