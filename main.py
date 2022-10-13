import telebot
import random
from telebot import types
#/start-описание того что может этот бот
#сделать 4 кнопки с разными животными
#рандомно присылаться будут картинки с животными

app= telebot.TeleBot("5314239083:AAHibJuGAbqEReCT8PEc4wpa-HxkfCe7dSc")
@app.message_handler(commands = ['start'])
def start(message):
    app.send_message(message.chat.id, f'Привет! Меня зовут Базант и я буду радовать тебя своей коллекцией картинок. Отправь команду /board, и выбери то, что хочешь посмотреть! \n Если ты нажал, а тебе не прислали, нажми еще раз и еще раз)))0)0)')

@app.message_handler(commands = ['board'])
def board(message):
    markup = types.ReplyKeyboardMarkup()
    btt = types.KeyboardButton('Мемасик')
    btt2 = types.KeyboardButton("Капибара")
    btt3 = types.KeyboardButton("Лама")
    btt4 = types.KeyboardButton("Котик")
    markup.add(btt, btt2, btt3, btt4)
    app.send_message(message.chat.id, "Выбирай!", reply_markup = markup)

@app.message_handler(content_types= ['text'])
def otvet(message):
    if message.text == "Мемасик":
        x = str(random.randrange(1, 32))
        photo = open('Мем'+x+".jpg", 'rb')
        app.send_photo(message.chat.id, photo)
    elif message.text == "Капибара":
        y = str(random.randrange(1, 180))
        photo = open("Капибара" + y + ".jpg", 'rb')
        app.send_photo(message.chat.id, photo)
    elif message.text == "Лама":
        x = str(random.randrange(1, 98))
        photo = open("Лама" + x + ".jpg", 'rb')
        app.send_photo(message.chat.id, photo)
    elif message.text == "Котик":
        x = str(random.randrange(1, 98))
        photo = open("Котик" + x + ".jpg", 'rb')
        app.send_photo(message.chat.id, photo)


app.polling(none_stop=True)