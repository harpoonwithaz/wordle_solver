import os
from dotenv import load_dotenv

# Discord bot imports
import discord
from discord import app_commands
from discord.ext import commands

# load token from safe file
load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')

# Loads bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '%', intents = discord.Intents.default())

# Attempts to sync commands on start
@bot.event
async def on_ready():
    print(f'{bot.user} is now running')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

# Command to sync all the commands
# THIS COMMAND DOESN'T WORK
@bot.tree.command(name='sync')
async def sync(interaction: discord.Integration):
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
        await interaction.response.send_message(f'Successfully synced {len(synced)} command(s)')
    except Exception as e:
        print(e)
        await interaction.response.send_message(f'Sync failed: {e}')

# Testing command
@bot.tree.command(name='test')
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f'Hello {interaction.user.mention}')

# Wordle game command
@bot.tree.command(name='play')
async def play(interaction: discord.Integration):
    
    embed = discord.Embed(description="helllo lol \n<:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783>\n<:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783>\n<:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783>\n<:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783>\n<:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783>\n<:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783><:black_medium_square:1324633733474549783>",
                        colour=0x00b0f4)

    embed.set_author(name="testing")

    await interaction.response.send_message(embed=embed)

# Runs bot with token from .env file
bot.run(bot_token)