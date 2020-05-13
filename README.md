# Curse Watcher Bot for Telegram

This is a little bot for Telegram messenger which is watching for bad words.

## Before Starting

### Create Bot and Generate Token
In Telegram app or web app, start chatting with: https://t.me/botfather
Then use the /newbot to create a bot and generate the TOKEN

Also, you need to DISABLE privacy settings. For that just tell the BotFather: /setprivacy
 
### Add Bot to your favorite Group
Just invite your newly created bot to the group you wish to watch for curses.

### Create Word List
Add your favorite (!) words to "bad_word.csv" file

## Up and running
### Set Token and Warning Message
Change in code or set as environment variable:

 - BOT_TOKEN
 - WARNING_MESSAGE

### Installation

Install Python (tested with 3.8)
pip install -r requirements.txt

#### Run the Service

This service should be left up and running.
```python main.py```

### Docker
```
docker run --rm \
-e BOT_TOKEN=your-toke-here \
-e WARNING_MESSAGE="Please!!! Language!!!" \
mbooali/curse-watcher:1.0.0
```

```
# optional local build
docker build .
```