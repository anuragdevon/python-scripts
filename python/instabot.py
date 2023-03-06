#!usr/bin/python3

# instabot for posting photo to instagram
from instabot import Bot

bot = Bot()

bot.login(username = "user_name", password = "user_password")

# put the photo in the same directory as the python file
# or else have tp provide the path

bot.upload_photo("youtphoto.extension", caption = "your caption here")

