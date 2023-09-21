# Shellcord
> Shell based Discord 'client' \
> Special thanks to `User-31415` for help in debugging code.

### Early concept of post / get terminal 'client'
<img src="https://i.imgur.com/5WX5KMf.png" alt="image" width="400" height="350"> \
### Basic Webhook
<img src="https://i.imgur.com/CRP6BFt.png" alt="image" width="400" height="350">

## Howto
- post.py ~ client -> server
- get.py ~ server -> client
- hook.py ~ Simple webhook (can pass text & media files as payload in messages)
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
