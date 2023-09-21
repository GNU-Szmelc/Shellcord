# Shellcord
> Discord Bot / Hook 'client' for console 

## Howto
- `post.py` ~ client -> server
> c2s v4 / media & file as a payload \
> Post on Server/Channel as BOT from local terminal
```
usage: post.py
Enter the message you want to send 
([media] to send files / or [exit] to quit): media
Enter the path to the media file (e.g., image.jpg): image.jpg
```
- `get.py` ~ server -> client
> "Listen to" Server chat in local terminal
- `hook.py` ~ Simple webhook
> Webhook can pass text & media files as payload in message
```
usage: hook.py [-h] [--message MESSAGE] [--file FILE] [--log LOG]

Send messages to a Discord webhook or log messages to a file.

options:
  -h, --help            show this help message and exit
  --message MESSAGE, -m MESSAGE
                        The message to send to Discord.
  --file FILE, -f FILE  The path to a file containing messages to
                        send to Discord.
  --log LOG, -l LOG     Log messages to a file.
```
## Screenshots
### Early concept of post / get terminal 'client'
<img src="https://i.imgur.com/aysNIkv.png" alt="image" width="400" height="350"> \
### Basic Webhook [v2]
<img src="https://i.imgur.com/CRP6BFt.png" alt="image" width="400" height="350"> \
### Example Bot post.py [v4]
<img src="https://i.imgur.com/IBsTjEj.png" alt="image" width="400" height="350">
<img src="https://i.imgur.com/yzqxb7Y.png" alt="image">

> Special thanks to `User-31415` for help in debugging code.
