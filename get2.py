import discord
from discord.ext import commands
from colorama import Fore, Style, init
import os
import re

# Initialize colorama
init(autoreset=True)

# Set intents
intents = discord.Intents.default()
intents.messages = True
intents.guild_messages = True
intents.message_content = True

# Create a bot instance with intents
bot = commands.Bot(command_prefix='/', intents=intents)

# Define an event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.slash_command.create_all()

# Define an event for when a message is received
@bot.event
async def on_message(message):
    author = message.author
    nickname = author.nick if author.nick else author.name
    channel_name = message.channel.name

    # Define colors
    channel_color = Fore.CYAN
    nickname_color = Fore.GREEN
    content_color = Fore.YELLOW

    # Handle attachments
    attachment_str = ""
    if message.attachments:
        attachment_str = " ".join([f'[Image]({attachment.url})' for attachment in message.attachments])

    # Handle embeds (links)
    embed_str = ""
    if message.embeds:
        embed_str = " ".join([f'[Link]({embed.url})' for embed in message.embeds if embed.type == 'link'])

    # Handle URLs in message content
    url_str = " ".join([f'[URL]({url.group(0)})' for url in re.finditer(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)])

    # Print with colors
    print(f'\n{channel_color}[{channel_name}]{Style.RESET_ALL} '
          f'\n{nickname_color}[{nickname}]:{Style.RESET_ALL} '
          f'\n{content_color}{message.content}{Style.RESET_ALL} '
          f'{attachment_str} {embed_str} {url_str}')

    await bot.process_commands(message)

# Other commands remain the same

bot.run('YOUR_BOT_TOKEN')
