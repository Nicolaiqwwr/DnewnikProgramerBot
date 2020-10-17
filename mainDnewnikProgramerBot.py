import telebot
import time

bot = telebot.TeleBot(':AAH0GdoQSt_f4tsW4ydjzS69kVG8dx94UIA', parse_mode=None)


description_chat = """Правила чата:
https://t.me/rulesofdnevnikprogram
Должности чата:
https://t.me/doljnostidnevnika
Сотрудничество:
telegramernest@gmail.com
Основной канал:
https://t.me/dnevnikprogram
                """


rules_chat = """Запрещены:
1. Мат и прочие ругательства на всех языках запрещены!
2. Нежелательные выражения ( слова которые не щитаються матами. )
( Слова и выражения которые могут затронуть быть неприемлемы для некоторых людей )
3. Порнография
4. Спам
5. Подозрительные рассылки
6. Реклама без согласования с администрацией
7. Жестокий контент
8. Оскорбление пользователей
9. Расизм и сексизм ( ущемление по провам в чате девушек , людей других наций , стран , цвета кожи групп и тд  )
"""

botPower = """Навыки бота:
1) Вывод по тегу /rules правил чата
2) Вывод по тегу /description описание чата
3) Вывод по тегу /allComands всех команд доступных пользователям чата
3) Вывод по тегу /botPower описание способностей бота

Запланировано:
1-Автоматический вывод сообщений ботом
2-Репортин
3-Автобаны
4-миниигры
"""
allComands = """
/start
/rules
/allComands
/botPower
"""

@bot.message_handler(commands=['start'])
def handler_commands(message):
    bot.send_message(message.chat.id, "Приветствую {0.first_name}".format(message.from_user),
                     parse_mode='html')
    bot.send_message(message.chat.id, "Ознакомся с командами {0}".format(allComands),
                     parse_mode='html')
    bot.send_message(message.chat.id, "А также незабудь прочитать правила чата {0}".format(rules_chat),
                     parse_mode='html')
    time.sleep(5)

@bot.message_handler(commands=['description'])
def handler_commands(message):
    bot.send_message(message.chat.id, 'Описание чата:/n{0}'.format(description_chat),
                     parse_mode='html')

@bot.message_handler(commands=['rules'])
def handler_commands(message):
    bot.send_message(message.chat.id, rules_chat,
                     parse_mode='html')
    time.sleep(5)

@bot.message_handler(commands=['allComands'])
def handler_commands(message):
    bot.send_message(message.chat.id, allComands,
                     parse_mode='html')
    time.sleep(5)

@bot.message_handler(commands=['botPower'])
def handler_commands(message):
    bot.send_message(message.chat.id, botPower,
                     parse_mode='html')
    time.sleep(5)


#RUN
bot.polling(none_stop=True)
