import requests
import json
import os

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = '[YOUR BOT TOKEN]'

# Replace 'YOUR_CHANNEL_ID' with the channel ID where you want to send the message
CHANNEL_ID = '[YOUR CHANNEL ID]'

# Discord API endpoint for sending messages
DISCORD_API_URL = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'

while True:
    # Get user input for the message content
    message_content = input("Enter the message you want to send (or 'exit' to quit): ")

    if message_content.lower() == 'exit':
        break

    # Create the JSON payload for the message
    payload = {
        'content': message_content
    }

    # Define headers with the bot's token
    headers = {
        'Authorization': f'Bot {TOKEN}',
        'Content-Type': 'application/json'
    }

    # Send the HTTP POST request to send the message
    response = requests.post(DISCORD_API_URL, data=json.dumps(payload), headers=headers)

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Error sending message. Status code: {response.status_code}')
        print(response.text)

    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')
