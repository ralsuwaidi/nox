import logging
from os import environ as env
import os
import telebot
import nox.utils as utils

from nox.txt2img import Txt2img

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(env["NOX_BOT_KEY"])

@bot.message_handler(commands=['commands', 'options'])
def show_commands(message):
	bot.reply_to(message, Txt2img.show_all_options())

@bot.message_handler(commands=['ink'])
def draw_ink(message):
    utils.draw_with_command(bot, message, "ink")

@bot.message_handler(commands=['comic'])
def draw_comic(message):
    utils.draw_with_command(bot, message, "comic")

@bot.message_handler(commands=['samu'])
def draw_samu(message):
    utils.draw_with_command(bot, message, "samu")

@bot.message_handler(commands=['models'])
def show_ai_models(message):
	bot.reply_to(message, Txt2img.show_ai_models())


@bot.message_handler(func=lambda message: True)
def draw(message):

    utils.draw_with_command(bot, message)

    # if txt2img.all_details:
    #     for i in ["high", "alpha", "beta", "gamma"]:
    #         prompt = message.text + " detailed:" + i
    #         txt2img = Txt2img(prompt)
    #         photo_file = txt2img.gen_image()
    #         photo = open(photo_file, "rb")

    #         bot.send_photo(message.chat.id,
    #                             photo=photo)
          



bot.infinity_polling(timeout=560, long_polling_timeout=1200)
