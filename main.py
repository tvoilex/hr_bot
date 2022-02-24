import telebot
import datetime
import random
import pymongo
from telebot import types
import os
import sys, time
bot = telebot.TeleBot("5167494720:AAEHZKljDqz5nMvCaa7IQTLCSD0EPr4ghn4")
mongo = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = mongo["hr_bot"]
mycollection = mydb["users"]







# bot.send_message(member, message.text[message.text.find(' ') + 1:])

admin_id = 1521078132

users = list(mycollection.find())
print(users)

directory = "vacancy"
vacancys = os.listdir(directory)





# def notify(message):
#     joinedFile = open('all_id.txt', 'r')
#     joinedUsers = set()
#     for line in joinedFile:
#         joinedUsers.add(line.strip())
#     joinedFile.close()
#     print(joinedUsers)
#
#     command_sender = message.from_user.id
#     if command_sender in admin_id:
#         with open('unique_id.txt', 'r') as ids:
#             for line in ids:
#                 user_id = int(line.strip("\n"))
#                 try:
#                     bot.send_message(user_id,  f'уведомление от {command_sender}')
#                 except Exception as e:
#                     bot.send_message(command_sender, f'ошибка отправки сообщения юзеру - {user_id}')
#     else:
#         bot.send_message(command_sender, f'у вас нет прав для запуска команды')


@bot.message_handler(commands=["start"])




def welcome(message):
    newuser = {"id" : message.from_user.id}
    x = mycollection.insert_one(newuser)



    with open("all_id.txt", "a") as all_id:
        all_id.write(f"{message.chat.id}\n") #запись user_id в общий файл
        all_id.close()
        lines_set = set()
    with open("all_id.txt", "r") as all_id, open("unique_id.txt", "w") as unique:
        for line in all_id:
            if line not in lines_set:
                unique.write(line)
            lines_set.add(line)
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Найти работу"))
    msg = bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе найти работу! Если Вы хотите найти работу - напишите 'Найти работу'".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=rmk)
    with open(f"users/{message.from_user.id}.txt", 'w') as file:
        file.write(f"ID - {message.from_user.id}\n")
        file.write(f"Username - {message.from_user.username}\n")
        bot.register_next_step_handler(msg, preludia)

# @bot.message_handler(commands=["special"])
# def send(message):
#     for user in joinedUsers:
#         bot.send_message(user, message.text[message.text.find(''):])





@bot.message_handler(content_types=["text"])



def preludia(message):
    if message.text == "Найти работу":
        msg = bot.send_message(message.chat.id, "Требуется ответить на несколько вопросов")
        bot.send_message(message.chat.id, "Вопрос 1: Ваше *имя*?", parse_mode="Markdown")
        bot.register_next_step_handler(msg, q2)

def q2(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Очень приятно! Укажите Ваш пол", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Имя - {message.text}\n")
    bot.register_next_step_handler(msg, q3)
    if message.text == "/start":
        bot.register_next_step_handler(msg, welcome)


def q3(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Укажите Ваше гражданство", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Пол - {message.text}\n")
    bot.register_next_step_handler(msg, q4)

def q4(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Укажите город проживания", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Гражданство - {message.text}\n")
    bot.register_next_step_handler(msg, q5)

def q5(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Укажите город, где хотите работать", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Город - {message.text}\n")
    bot.register_next_step_handler(msg, q6)

def q6(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Есть ли у Вас виза? Если да, то какая?", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Желаемый город - {message.text}\n")
    bot.register_next_step_handler(msg, q7)

def q7(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Имеется ли жильё в предпологаемом месте работы?", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Виза - {message.text}\n")
    bot.register_next_step_handler(msg, q8)

def q8(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Имеется ли у Вас образование? Укажите какое", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Жильё в желаемом городе - {message.text}\n")
    bot.register_next_step_handler(msg, q9)

def q9(message):
    print(message.text)
    msg = bot.send_message(message.chat.id, "Какого характера работа Вас интересует?", parse_mode="Markdown")
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Образование - {message.text}\n")
    bot.register_next_step_handler(msg, q10)

def q10(message):
    print(message.text)
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Подтвердить"))
    msg = bot.send_message(message.chat.id, "Спасибо! Напишите 'подтвердить', если данные верны!", parse_mode="Markdown", reply_markup=rmk)
    with open(f"users/{message.from_user.id}.txt", 'a') as file:
        file.write(f"Желаемый тип работы - {message.text}\n\n\n")
    with open(f"users/{message.from_user.id}.txt", 'r') as file:
        content = file.read()
   # secret = bot.send_message("487082863", content)
    secret2 = bot.send_message("1521078132", content)
    bot.register_next_step_handler(msg, q11)

def q11(message):

    string = "/a"

    msg = bot.send_message(message.chat.id, 'Принято', parse_mode="Markdown")

    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Подтвердить"))
    if message.text == "Подтвердить" and message.from_user.id == admin_id:
        print('admin is entered')
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Доступные вакансии')
        ).add(
            types.KeyboardButton('Написать в поддержку')
        ).add(
            types.KeyboardButton('Заполнить анкету заново')
        ).add(
            types.KeyboardButton('Отправить уведомление')
        )
        bot.send_message(message.chat.id,'Теперь Вам доступны опции "Написать в поддержку" и "посмотреть вакансии"'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup_request)
        bot.register_next_step_handler(msg, menu1)
    elif message.text == "Подтвердить":
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Доступные вакансии')
        ).add(
            types.KeyboardButton('Написать в поддержку')
        ).add(
            types.KeyboardButton('Заполнить анкету заново')
        )
        bot.send_message(message.chat.id,'Теперь Вам доступны опции "Написать в поддержку" и "посмотреть вакансии"'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup_request)
        bot.register_next_step_handler(msg, menu1)

    else:
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Доступные вакансии')
        ).add(
            types.KeyboardButton('Написать в поддержку')
        ).add(
            types.KeyboardButton('Заполнить анкету заново')
        )
        bot.send_message(message.chat.id,'Теперь Вам доступны опции "Написать в поддержку" и "посмотреть вакансии"'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup_request)
        bot.register_next_step_handler(msg, menu1)

def menu1(message):
    while message.text:
        string = "/a"
        if message.text == 'Написать в поддержку':
            msg = bot.send_message(message.chat.id,"@NikRB", parse_mode="Markdown")
            bot.register_next_step_handler(msg, menu1)
            break

        elif message.text == 'Доступные вакансии':
            rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            rmk.add(types.KeyboardButton("Получить все вакансии"))
            msg = bot.send_message(message.chat.id,"Просмотреть доступные вакансии?", parse_mode="Markdown", reply_markup=rmk)
            bot.register_next_step_handler(msg, vacancy)
            break

        elif message.text == 'Заполнить анкету заново':
            markup_request = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(
                types.KeyboardButton('Отмена')
            ).add(
                types.KeyboardButton('Заполнить анкету заново')
            )
            msg = bot.send_message(message.chat.id, 'Начать заново?'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup_request)
            bot.register_next_step_handler(msg, repeat)
            break

        elif message.text == 'Отправить уведомление':
            # for member in users:
            a = mycollection.distinct("id")
            print(a)
            for users in a:
                msg = bot.send_message(users, "реклама", parse_mode="Markdown")
                bot.register_next_step_handler(msg, menu1)
            break

        else:
            msg = bot.send_message(message.chat.id, "выберете один из пунктов", parse_mode="Markdown")
            bot.register_next_step_handler(msg, menu1)
            break
# def noti(message):
#     rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     rmk.add(types.KeyboardButton("назад"))
#     for user in users:
#         msg = bot.send_message(user, message.text[message.text.find(' '):])
#         bot.register_next_step_handler(msg, q10)
#         break



def repeat(message):
    if message.text == 'Заполнить анкету заново':
        rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        rmk.add(types.KeyboardButton("Подтвердить"))
        msg = bot.send_message(message.chat.id, "Начнём заново!", parse_mode='Markdown', reply_markup=rmk)
        bot.register_next_step_handler(msg, welcome)
    else:
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Доступные вакансии')
        ).add(
            types.KeyboardButton('Написать в поддержку')
        ).add(
            types.KeyboardButton('Заполнить анкету заново')
        )
        msg = bot.send_message(message.chat.id, "Выберите один из пунктов", parse_mode='html', reply_markup=markup_request)
        bot.register_next_step_handler(msg, menu1)

def vacancy(message):
    dirname = "vacancy"
    files = os.listdir(dirname)
    lenth_of_vacancy = len(files)
    i = 0
    for filename in os.listdir("vacancy"):
        with open(os.path.join("vacancy", filename), 'r') as f:
            while i != lenth_of_vacancy:
                text = f.read()
                msg = bot.send_message(message.chat.id, text, parse_mode='Markdown')
                i = i+1
                break
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Назад"))
    msg = bot.send_message(message.chat.id,"Хотите вернуться назад?", parse_mode="Markdown", reply_markup=rmk)
    bot.register_next_step_handler(msg, q11)

# @bot.message_handler(commands=["a"])
# def mess(message):
#     for user in users:
#         a = list(mycollection.find({}))
#         print(a)






while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
