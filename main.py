import telebot
from telebot import types
import requests
client = telebot.TeleBot("5179136573:AAFoRy-MQ1Pm_hMEZY3eUo7l2CKLpx6bNYg")


@client.message_handler(commands=["start"])

def welcome(message):


    with open("all_id.txt", "a") as all_id:
        all_id.write(f"{message.from_user.id}\n") #запись user_id в общий файл
        all_id.close()
        lines_set = set()
    with open("all_id.txt", "r") as all_id, open("unique_id.txt", "w") as unique:
        for line in all_id:
            if line not in lines_set:
                unique.write(line)
            lines_set.add(line)
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Найти работу"))
    msg = client.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе найти работу! Если Вы хотите найти работу - напишите 'Найти работу'".format(message.from_user, client.get_me()), parse_mode='html', reply_markup=rmk)
    with open(f"{message.from_user.username}.txt", 'w') as file:
        file.write(f"ID - {message.from_user.id}\n")
        file.write(f"Username - {message.from_user.username}\n")
        client.register_next_step_handler(msg, preludia)




@client.message_handler(content_types=["text"])

def preludia(message):
    if message.text == "Найти работу":
        msg = client.send_message(message.chat.id, "Требуется ответить на несколько вопросов")
        client.send_message(message.chat.id, "Вопрос 1: Ваше *имя*?", parse_mode="Markdown")
        client.register_next_step_handler(msg, q2)
    # else:
    #     client.send_message(message.chat.id, "хуй")


def q2(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Очень приятно! Укажите Ваш пол", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q3)
    if message.text == "/start":
        client.register_next_step_handler(msg, welcome)
def q3(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Укажите Ваше гражданство", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q4)
def q4(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Укажите город проживания", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q5)
def q5(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Укажите город, где хотите работать", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q6)
def q6(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Есть ли у Вас виза? Если да, то какая?", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q7)
def q7(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Имеется ли жильё в предпологаемом месте работы?", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q8)
def q8(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Имеется ли у Вас образование? Укажите какое", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q9)
def q9(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Какого характера работа Вас интересует?", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q10)
def q10(message):
    print(message.text)
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Подтвердить"))
    msg = client.send_message(message.chat.id, "Спасибо! Напишите 'подтвердить', если данные верны!", parse_mode="Markdown", reply_markup=rmk)
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n\n\n")
    client.register_next_step_handler(msg, q11)
def q11(message):
    with open(f"{message.from_user.username}.txt", 'r') as file:
        content = file.read()
    msg = client.send_message(message.chat.id, 'кек', parse_mode="Markdown")
    secret = client.send_message("487082863", content)
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Подтвердить"))
    if message.text == "Подтвердить":
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Доступные вакансии')
        ).add(
            types.KeyboardButton('Написать в поддержку')
        ).add(
            types.KeyboardButton('Заполнить анкету заново')
        )
        client.send_message(message.chat.id,'Теперь Вам доступны опции "Написать в поддержку" и "посмотреть вакансии"'.format(message.from_user, client.get_me()), parse_mode='html', reply_markup=markup_request)
        client.register_next_step_handler(msg, menu1)
    else:
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Доступные вакансии')
        ).add(
            types.KeyboardButton('Написать в поддержку')
        ).add(
            types.KeyboardButton('Заполнить анкету заново')
        )
        client.send_message(message.chat.id,'Теперь Вам доступны опции "Написать в поддержку" и "посмотреть вакансии"'.format(message.from_user, client.get_me()), parse_mode='html', reply_markup=markup_request)
        client.register_next_step_handler(msg, menu1)

def menu1(message):
    while message.text:
        if message.text == 'Написать в поддержку':
            msg = client.send_message(message.chat.id,"@NikRB", parse_mode="Markdown")
            client.register_next_step_handler(msg, menu1)
            break
        elif message.text == 'Доступные вакансии':
            msg = client.send_message(message.chat.id,"Доступные вакансии:", parse_mode="Markdown")
            client.register_next_step_handler(msg, menu1)
            break
        elif message.text == 'Заполнить анкету заново':
            markup_request = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(
                types.KeyboardButton('Отмена')
            ).add(
                types.KeyboardButton('Заполнить анкету заново')
            )
            msg = client.send_message(message.chat.id, 'Начать заново?'.format(message.from_user, client.get_me()), parse_mode='html', reply_markup=markup_request)
            client.register_next_step_handler(msg, repeat)
            break
        else:
            msg = client.send_message(message.chat.id, "выберете один из пунктов", parse_mode="Markdown")
            client.register_next_step_handler(msg, menu1)
            break
def repeat(message):
    if message.text == 'Заполнить анкету заново':
        rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        rmk.add(types.KeyboardButton("Подтвердить"))
        msg = client.send_message(message.chat.id, "Начнём заново!", parse_mode='Markdown', reply_markup=rmk)
        client.register_next_step_handler(msg, welcome)
    else:
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Доступные вакансии')
        ).add(
            types.KeyboardButton('Написать в поддержку')
        ).add(
            types.KeyboardButton('Заполнить анкету заново')
        )
        msg = client.send_message(message.chat.id, "Выберите один из пунктов", parse_mode='html', reply_markup=markup_request)
        client.register_next_step_handler(msg, menu1)
            # rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            # rmk.add(types.KeyboardButton("Начать заново"))
            # msg = client.send_message(message.chat.id, "Начать заново?".format(message.from_user, client.get_me()), parse_mode='html', reply_markup=rmk)
            # client.register_next_step_handler(msg, welcome)



#def m2(message): парсинг с файла, в который заливает другой бот







client.infinity_polling()