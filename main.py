import telebot
from telebot import types
import requests

client = telebot.TeleBot("5179136573:AAFoRy-MQ1Pm_hMEZY3eUo7l2CKLpx6bNYg")

@client.message_handler(commands=["start"])

def welcome(message):
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
        client.register_next_step_handler(msg, q1)
    else:
        client.send_message(message.chat.id, "Я Вас не понимаю")

def q1(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Напишите свою *фамилию*", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q2)

def q2(message):
    print(message.text)
    msg = client.send_message(message.chat.id, "Очень приятно! Укажите Ваш пол", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n")
    client.register_next_step_handler(msg, q3)
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
    msg = client.send_message(message.chat.id, "Спасибо!", parse_mode="Markdown")
    with open(f"{message.from_user.username}.txt", 'a') as file:
        file.write(f"{message.text}\n\n\n")
    client.register_next_step_handler(msg, q11)
def q11(message):
    with open(f"{message.from_user.username}.txt", 'r') as file:
        content = file.read()
    client.send_message("1521078132", content)






client.polling()