import requests
import json
import os

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = 'YOUR_BOT_TOKEN'

# Replace 'YOUR_CHANNEL_ID' with the channel ID where you want to send the message
CHANNEL_ID = 'YOUR_CHANNEL_ID'

# Discord API endpoint for sending messages
DISCORD_API_URL = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'

def send_message_with_media(content, file_path):
    # Create the multipart payload for the message with media file
    payload = {
        'content': content,
    }

    files = {
        'file': open(file_path, 'rb')
    }

    # Define headers with the bot's token
    headers = {
        'Authorization': f'Bot {TOKEN}',
    }

    # Send the HTTP POST request to send the message with media
    response = requests.post(DISCORD_API_URL, data=payload, files=files, headers=headers)

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Error sending message. Status code: {response.status_code}')
        print(response.text)

while True:
    # Get user input for the message content
    message_content = input("Enter the message you want to send \n([media] to send files / or [exit] to quit): ")

    if message_content.lower() == 'exit':
        break

    # Check if user wants to send a media file
    if message_content.lower() == 'media':
        file_path = input("Enter the path to the media file (e.g., image.jpg): ")
        send_message_with_media('Check out this media file!', file_path)
    else:
        # Create the JSON payload for a regular text message
        payload = {
            'content': message_content,
        }

        # Define headers with the bot's token
        headers = {
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json',
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
