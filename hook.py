import argparse
import requests
import mimetypes

# Replace this with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url_here"

def send_message_to_discord(message, file_paths=[]):
    payload = {"content": message}
    files = []

    for file_path in file_paths:
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type:
            files.append(("file", (file_path, open(file_path, "rb"), mime_type)))

    response = requests.post(WEBHOOK_URL, data=payload, files=files)

    if response.status_code == 204:
        print("Message sent successfully to Discord.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

def main():
    parser = argparse.ArgumentParser(description="Send messages and media files to a Discord webhook.")
    parser.add_argument("--message", "-m", help="The message to send to Discord.")
    parser.add_argument("--file", "-f", nargs="*", help="The path to media files to send to Discord.")
    parser.add_argument("--log", "-l", help="Log messages to a file.")

    args = parser.parse_args()

    if args.message:
        send_message_to_discord(args.message, args.file)
    elif args.file:
        send_message_to_discord("Uploaded media:", args.file)
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
