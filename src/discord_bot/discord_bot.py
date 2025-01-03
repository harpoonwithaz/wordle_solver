import os
from dotenv import load_dotenv

# Discord bot imports
import discord
from discord import app_commands
from discord.ext import commands

# Local imports
import embed_container

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
async def test(interaction: discord.Integration):
    await interaction.response.send_message(f'Hello <:yi:1324849058832977972>')

# Command to give wordle tutorial
@bot.tree.command(name='tutorial')
async def tutorial(interaction: discord.Integration):
    
    embed = embed_container.tutorial()
    await interaction.response.send_message(embed=embed)


# Runs bot with token from .env file
bot.run(bot_token)