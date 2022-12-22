import random
import time
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Получить ответ')
    item2 = telebot.types.KeyboardButton('Кинуть кости)')
    item3 = telebot.types.KeyboardButton('Заново')
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     'Привет, Я волшебный шар с ответами, задай мне вопрос на "да" или "нет", ну или просто сконцентрируйся на своем вопросе и нажми на кнопочку!',
                     reply_markup=markup)
    bot.send_message(message.chat.id, 'Внимание! Не использовать в качестве теста на беременность!!!')
    bot.send_message(message.chat.id,
                     'А еще я могу кидать кости) очень удобно, если нужно дрюкнуть кого-нибудь в нарды, а зарики потерялись)',
                     reply_markup=markup)


def random_numbers(message):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    bot.send_message(message.chat.id, f'Выпало {str(num1)} и {str(num2)}')
    if num1 == num2:
        bot.send_message(message.chat.id, f'Ого, да это {str(num1)} куш! Тебе сегодня везет!!!')


def magic_ball(message):
    answers = ["Однозначно только так!", "Так решено свыше!", "Вааще не сомневайся!", "Определенно ДА",
               "Можешь быть в этом уверен!",
               "Кажется да, но когда <<кажется>> - сами знаете...", "Ну, скорее всего", "Отличные перспективы)",
               "Знаки говорят ДА", "ДААААА!!!", "Пока непонятно -_-", "Спроси попозже",
               "Лучше тебе пока об этом не знать :/",
               "Сейчас ничего нельзя сказать однозначно", "Помехи какие-то, ну-ка повтори еще разок", "Даже не думай!",
               "НЕЕЕЕТ!!!", "Мои аналитики говорят - нет", "Перспективы не радуют(", "Весьма сомнительно"]
    doubts = ["Давай-ка посмотрим...", "Ща гляну...", "Ну-ка, ну-ка...", "Тээээкс...", "Пурум-пум-пум...",
              "Ну и вопросик...",
              "Спросим у духов...", "Так-так-так...", "Че там у нас?..", "Эээмммм...", "Минуточку...", "........",
              "Провожу аналитику..."]
    bot.send_message(message.chat.id, random.choice(doubts))
    time.sleep(2)
    bot.send_message(message.chat.id, random.choice(answers))


@bot.message_handler(content_types=['text'])
def sent_text(message):
    if message.text == 'Кинуть кости)':
        random_numbers(message)
    elif message.text == 'Заново':
        welcome(message)
    else:
        magic_ball(message)


bot.polling(none_stop=True)
