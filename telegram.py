import logging
from os import environ as env
import os
import telebot

from nox.txt2img import Txt2img

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(env["NOX_BOT_KEY"])

@bot.message_handler(commands=['commands', 'options'])
def show_commands(message):
	bot.reply_to(message, Txt2img.show_all_options())

@bot.message_handler(commands=['models'])
def show_ai_models(message):
	bot.reply_to(message, Txt2img.show_ai_models())


@bot.message_handler(func=lambda message: True)
def draw(message):

    txt2img = Txt2img(message.text)

    txt2img.update_response()
    bot.send_message(message.chat.id,
                     f'{txt2img.response}')

    # send uploading
    bot.send_chat_action(message.chat.id, "upload_photo")

    for i in range(txt2img.repeat):
        photo_file = txt2img.gen_image()
        if photo_file is not None:
            photo = open(photo_file, "rb")

            bot.send_photo(message.chat.id,
                            photo=photo)
            
            try:
                os.remove(photo_file) 
            except:
                pass

    if txt2img.all_details:
        for i in ["high", "alpha", "beta", "gamma"]:
            prompt = message.text + " detailed:" + i
            txt2img = Txt2img(prompt)
            photo_file = txt2img.gen_image()
            photo = open(photo_file, "rb")

            bot.send_photo(message.chat.id,
                                photo=photo)
          



bot.infinity_polling(timeout=560, long_polling_timeout=1200)
