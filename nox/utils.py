import re
import os
from nox.txt2img import Txt2img


def get_opt(prompt: str):
    """get options as a dict"""
    options = {}
    parsed = prompt.split(" ")
    for i in parsed:
        if ":" in i:
            arg_split = i.split(":")
            if arg_split[0] != "" and arg_split[1] != "":
                try:
                    arg_split[1] = int(arg_split[1])
                except:
                    pass
                options[arg_split[0]] = arg_split[1]

    return(options)


def remove_opt(prompt: str):
    prompt_text = prompt
    parsed = prompt.split(" ")
    for i in parsed:
        if ":" in i:
            arg_split = i.split(":")
            print(i)
            if arg_split[0] != "" and arg_split[1] != "":
                prompt_text = prompt_text.replace(i,"")

    # remove double spacing
    prompt_text = re.sub(' +', ' ', prompt_text)

    return prompt_text

def is_too_large(prompt: str):
    if len(prompt.split(" ")) > 1400:
        return True
    return False

def draw_with_command(bot, message, command=None):

    if command is not None:
        clean_text = message.text.replace("/" + command,"")
        txt2img = Txt2img(clean_text, model_sc=command)
    else:
        txt2img = Txt2img(message.text)

    bot.send_message(message.chat.id, f'{txt2img.response}')
    bot.send_message(message.chat.id, f'{txt2img.prompt}')

    bot.send_chat_action(message.chat.id, "upload_photo")
    
    for i in range(txt2img.repeat):
        photo_file = txt2img.gen_image()
        photo = open(photo_file, "rb")

        bot.send_photo(message.chat.id,
                        photo=photo)
        
        try:
            os.remove(photo_file) 
        except:
            pass