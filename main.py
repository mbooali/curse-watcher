import telegram
import time
import logging
import sys
import csv
import os


def filter_and_reply(bot, black_list, warning_message):
    with open('current_offset.txt', mode='r') as f:
        current_offset = int(f.read())

    updates = list(bot.getUpdates(offset=current_offset))

    for update in updates:
        current_offset = max(current_offset, int(update.update_id) + 1)
        if not update.message:
            continue
        if not update.message.text_html:
            continue

        text = update.message.text_html

        message_id = str(update.message.message_id)
        chat_id = update.message.chat.id
        for word in black_list:

            if word in text.lower():
                try:
                    print("detected: ", text)
                    bot.send_message(
                        text=warning_message,
                        chat_id=chat_id,
                        reply_to_message_id=message_id
                    )

                    break

                except Exception as e:
                    logging.error("Unexpected error:")
                    logging.error(sys.exc_info()[0])

    # update the max offset in the file
    with open('current_offset.txt', mode='w') as f:
        f.write(str(current_offset))


def main():
    token = os.getenv('BOT_TOKEN') or 'put your token here'
    warning_message = os.getenv('WARNING_MESSAGE') or 'Please!!! Language!!!'
    bot = telegram.Bot(token=token)

    # TODO: Load bad_words from a external endpoint
    # TODO: as word list could be much bigger than message, would be nice to
    #       store them in dictionary and look up each word from that dict.
    with open('bad_words.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        black_list = list(map(lambda x: x[0], data))

    while True:
        time.sleep(2)
        try:
            filter_and_reply(bot, black_list, warning_message)
        except telegram.error.TimedOut:
            pass


main()
