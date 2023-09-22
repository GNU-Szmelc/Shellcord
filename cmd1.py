import discord
from discord.ext import commands
from colorama import Fore, Style, init
import os

# Add `/` commands
# - /save_logs
# - /save_media
# - /bruh

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
    # Registering the slash commands for autocomplete
    await bot.slash_command.create_all()

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

# Define a command to save the last 10 messages to a local file
@bot.command(name='save_logs')
async def save_logs(ctx):
    messages = []  # Initialize a list to hold the messages
    async for message in ctx.channel.history(limit=10):  # Use an async for loop to iterate over the messages
        messages.append(message)  # Append each message to the list

    with open('log.txt', 'w', encoding='utf-8') as f:
        for message in reversed(messages):  # Reverse the list to maintain chronological order
            author = message.author.nick if hasattr(message.author, 'nick') and message.author.nick else message.author.name
            f.write(f'[{message.channel.name}] [{author}]: {message.content}\n')
    await ctx.send('Logs have been saved to log.txt')

# Define a command to save all media to a local folder
@bot.command(name='save_media')
async def save_media(ctx):
    media_folder = 'media'
    if not os.path.exists(media_folder):
        os.makedirs(media_folder)

    async for message in ctx.channel.history():
        for attachment in message.attachments:
            await attachment.save(os.path.join(media_folder, attachment.filename))
    await ctx.send('Media have been saved to media folder')

# Define a command to reply with a mention and a local image
@bot.command(name='bruh')
async def bruh(ctx):
    user_mention = ctx.author.mention
    file = discord.File('image.jpg', filename='image.jpg')
    await ctx.send(f'{user_mention} Bruh!', file=file)

bot.run("BOT_TOKEN")
