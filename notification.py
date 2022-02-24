# import telebot
# from telebot import types
# import os
# client = telebot.TeleBot("5102871746:AAGgmS1FbdigtLCH_EHh4GHBOECK3d3Vpmw")
# import main
#
# @client.message_handler(commands=["start"])
#
# def welcome(message):
#     rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     rmk.add(types.KeyboardButton("Разослать уведомления"))
#     msg = client.send_message(message.chat.id, "Привет, {0.first_name}!\nНажми 'Разослать уведомления'".format(message.from_user, client.get_me()), parse_mode='html', reply_markup=rmk)
#     client.register_next_step_handler(msg, n1)
#
#
# client.infinity_polling()