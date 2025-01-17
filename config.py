import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Open AI API Key
OPEN_AI_API_KEY = getenv("OPEN_AI_API_KEY", None)

# MidJourney API Key
MIDJOURNEY_KEY = getenv("MIDJOURNEY_KEY", None)

# Replicate API Key
REPLICATE_API_TOKEN = getenv("REPLICATE_API_TOKEN", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @mrootx on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5643634626))

# Set a Playlist Limit
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "10"))

LEAVE_TIME = int(getenv("LEAVE_TIME", "3600"))

SET_CMDS = getenv("SET_CMDS", "False")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Vinhzim/TrapLaudo-bot.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", False)

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/clubdaswinxcanal"
)  # Example:- https://t.me/politicament
SUPPORT_CHAT = getenv(
    "SUPPORT_GROUP", "https://t.me/winxmusicsupport"
)  # Example:- https://t.me/politicament

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False) == "True")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
STRING8 = getenv("STRING_SESSION8", None)
STRING9 = getenv("STRING_SESSION9", None)
STRING10 = getenv("STRING_SESSION10", None)


BANNED_USERS = filters.user()

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

# Images
START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://telegra.ph/file/a625772ae98cb351b789e.jpg",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://64.media.tumblr.com/e0de2ed5ab9aae5de7dc72b2fd4f1259/96d8ee5c67e607c2-66/s400x600/01388c517dd4d9e898e12dba1725cd0b83c04788.gifv",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://64.media.tumblr.com/e2e6eb90095d450447ff7ce607b18b55/b021ddfe0d679240-d9/s540x810/acbdb4ba69b40ea7755c8fdd7858c71e6aa31a9d.gifv",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://64.media.tumblr.com/b8e78bf58dec48e94792d174403e7649/15f4d0cf6aea574f-bd/s1280x1920/d7f85c27009a3a6fd1d4f930448580887b42c7a2.gifv",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://64.media.tumblr.com/78d65c97f6b13fd9e75751a6818f4bca/6817d36cce11d0ae-09/s540x810/17f6ee6542be0fea6eb332f1f0718bb3e7d2df80.gifv",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://64.media.tumblr.com/b8e78bf58dec48e94792d174403e7649/15f4d0cf6aea574f-bd/s1280x1920/d7f85c27009a3a6fd1d4f930448580887b42c7a2.gifv",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://64.media.tumblr.com/b8e78bf58dec48e94792d174403e7649/15f4d0cf6aea574f-bd/s1280x1920/d7f85c27009a3a6fd1d4f930448580887b42c7a2.gifv",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://64.media.tumblr.com/ea7bbbc05fe47c0306c2ac389eccc252/7724188deed06fee-a2/s1280x1920/3e5de4c6847843b79902a50a0873a58325551d55.gifv",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://64.media.tumblr.com/ea7bbbc05fe47c0306c2ac389eccc252/7724188deed06fee-a2/s1280x1920/3e5de4c6847843b79902a50a0873a58325551d55.gifv",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://64.media.tumblr.com/c39b07d55fbdff89661056be8bd08dbd/df2251522787e803-87/s1280x1920/40ae16b0ab0adadc2914146b115ab4ba0480863e.gifv",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://64.media.tumblr.com/73084dccbeffd73655bb3a07cef7904a/ca2e3db2a56b2f2d-71/s1280x1920/173c28fc197aef873f69df081e0671c35eacc9fb.gifv",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://64.media.tumblr.com/73084dccbeffd73655bb3a07cef7904a/ca2e3db2a56b2f2d-71/s1280x1920/173c28fc197aef873f69df081e0671c35eacc9fb.gifv",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://64.media.tumblr.com/73084dccbeffd73655bb3a07cef7904a/ca2e3db2a56b2f2d-71/s1280x1920/173c28fc197aef873f69df081e0671c35eacc9fb.gifv",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
