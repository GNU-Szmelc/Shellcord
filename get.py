import discord
from discord.ext import commands
from colorama import Fore, Style, init

# Set intents
intents = discord.Intents.default()
intents.messages = True
intents.guild_messages = True
intents.message_content = True

# Initialize colorama
init(autoreset=True)

# Create a bot instance with intents
bot = commands.Bot(command_prefix='/', intents=intents)

# Define an event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Define an event for when a message is received
@bot.event
async def on_message(message):
    # do stuff
    author = message.author
    nickname = author.nick if author.nick else author.name
    channel_name = message.channel.name

    # Define colors
    channel_color = Fore.CYAN
    nickname_color = Fore.GREEN
    content_color = Fore.YELLOW

    # Print with colors
    print(f'\n{channel_color}[{channel_name}]{Style.RESET_ALL} '
          f'\n{nickname_color}[{nickname}]:{Style.RESET_ALL} '
          f'\n{content_color}{message.content}{Style.RESET_ALL}')

    # Important: this ensures command processing is not broken by your custom on_message event
    await bot.process_commands(message)

# Run the bot with your token
bot.run('[YOUR BOT TOKEN]')
