import argparse
import requests

# Replace this with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/{CHANNEL ID}/{WEBHOOK TOKEN}"

def send_message_to_discord(message):
    payload = {"content": message}
    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        print("Message sent successfully to Discord.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

def main():
    parser = argparse.ArgumentParser(description="Send messages to a Discord webhook or log messages to a file.")
    parser.add_argument("--message", "-m", help="The message to send to Discord.")
    parser.add_argument("--file", "-f", help="The path to a file containing messages to send to Discord.")
    parser.add_argument("--log", "-l", help="Log messages to a file.")

    args = parser.parse_args()

    if args.message:
        send_message_to_discord(args.message)
    elif args.file:
        try:
            with open(args.file, "r") as file:
                messages = file.read().splitlines()
                for message in messages:
                    send_message_to_discord(message)
        except FileNotFoundError:
            print(f"File not found: {args.file}")
    elif args.log:
        try:
            with open(args.log, "a") as log_file:
                while True:
                    message = input("Enter a message to log (or 'q' to quit): ")
                    if message.lower() == "q":
                        break
                    log_file.write(message + "\n")
        except KeyboardInterrupt:
            pass
    else:
        print("Please provide a message, file, or log option. Use -h for help.")

if __name__ == "__main__":
    main()
