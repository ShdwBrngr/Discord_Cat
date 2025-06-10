# **Discord Cat Bot 🐾**
This is a personal project for building a multifunctional Discord bot using Python. It started as a learning project from the [Codedex Intermediate Python project](https://www.codedex.io/projects/build-a-discord-bot-with-python) and has since grown into a fun, meme-loving, cat-themed bot!

The bot currently supports basic commands for fetching memes, cat images, and includes a gacha-style "pull" system for collecting cat images. Future updates will include a collection system, crafting mechanics, and an in-bot currency system.

## **Features & Commands**
- `$meme` - Fetches a random meme from r/memes.
- `$imagefrom [subreddit]` - Fetches a random image from the specified subreddit.
- `$cat` - Returns a random cat picture from TheCatAPI.
- `$pull` - Gacha-style cat image pull with rarity tiers (common–epic).
- *Soon:* - `$collection` to view your collected cats.
- *Soon:* - `$craft` to combine a currency into a desired cat

## **Directory Structure**
```
Discord Cat/
├── .gitignore           # Files and directories excluded from Git tracking
├── cat_bot.py           # Main bot script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## **Future Plans**
- Cat Collection System: Track and view collected cats per user.
- Crafting System: Turn duplicates into a resource for crafting or upgrades.
- Currency & Pity System: Reward pulls and guarantee rare cats after repeated pulls.
- Gallery & Stats: View your cat gallery and gacha stats.

## **Technologies Used**
- Python 3
- discord.py – For building the Discord bot
- requests – For API calls
- dotenv – For managing API keys securely
- TheCatAPI, Meme API, and Pinterest – For content