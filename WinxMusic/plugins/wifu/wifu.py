import logging

import requests
from pyrogram import filters

from WinxMusic import app

WIFU_COMMAND = ["wifu", "waifu"]

# Define the API endpoint to fetch waifu images
API_ENDPOINT = "https://waifu.pics/api/sfw/waifu"


def waifu():
    try:
        response = requests.get(API_ENDPOINT)
        data = response.json()
        image_url = data["url"]
        return image_url
    except Exception as e:
        logging.error(str(e))


@app.on_message(filters.command(WIFU_COMMAND))
async def wifu(_, message):
    image_url = waifu()
    await message.reply_photo(image_url)
