import random
import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("6009027910:AAGkptIDNPADAAxQcfryhTleR4TMxFZUxRQ")
# Варианты ответов пользователю, если тот ввел непонятное боту сообщение
answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # Добавляем кнопки, которые будут появляться после ввода команды /start
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    button2 = types.KeyboardButton('⚙️ Настройки')
    button3 = types.KeyboardButton('📄 Справка')
    # Разделяю кнопки по строкам так, чтобы товары были отдельно от остальных кнопок
    markup.row(button1)
    markup.row(button2, button3)

    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые товары!\nКонтакт моего разработчика: https://t.me/neosome', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)

# Обработка фото. Если пользователь пришлет фото, то бот отреагирует на него. Можно реализовать свой функционал
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')

# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == '🛍 Товары':
        goodsChapter(message)
    elif message.text == '⚙️ Настройки':
        settingsChapter(message)
    elif message.text == '📄 Справка':
        infoChapter(message)
    elif message.text == '🍯 Липовый мед':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
        bot.send_message(message.chat.id, 'Мед обладает широким спектром применения, его в 1-ую очередь используют при простуде,также он применяется как общеукрепяющее средство и как отличное средство для устойчивой работы сердца.\n '
                                          
                                          'Объем и цены: 0.5=300р, 1л=600р, 1.5л=900р,5л=3000р. '
                                            'Оплата: https://www.tinkoff.ru/rm/dareshin.daniil1/xukM354656', reply_markup=markup)
    elif message.text == '🍯 Цветочный мед':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
        bot.send_message(message.chat.id, 'Мёд обладает целебным действием, усиливает обмен веществ, ускоряет восстановлению тканей, оказывает противовоспалительное, рассасывающее и бодрящее действие.\n '
                         'Объем и цены: 0.5=300р, 1л=600р, 1.5л=900р,5л=3000р. '
                         'Оплата: https://www.tinkoff.ru/rm/dareshin.daniil1/xukM354656',
                         reply_markup=markup)
    elif message.text == '🍯 Сотовый мед':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
        bot.send_message(message.chat.id, 'Мед в сотах особенно полезен, поскольку в нем присутствуют ценнейшие для здоровья вещества - прополис, воск, перга. В обработанном продукте такие компоненты отсутствуют, что по определению делает его свойства менее полезными\n '
                         'Объем и цены: 0.5=300р. '
                         'Оплата: https://www.tinkoff.ru/rm/dareshin.daniil1/xukM354656',
                         reply_markup=markup)
    elif message.text == '🍯 Настойка восковой моли':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
        bot.send_message(message.chat.id, 'Входящие в состав продукта элементы оказывают влияние на выносливость, способствуют ускорению роста мышечной массы, его применение активизирует выработку гемоглобина и скорость усвоения кальция.\n '
                                          'Объем и цены: 0.5=1750р. '
                                          'Оплата: https://www.tinkoff.ru/rm/dareshin.daniil1/xukM354656',
                         reply_markup=markup)
    elif message.text == '⚙️ Отзыв':
        # Функционал, чтобы пользователь оценил тг бота
        bot.send_message(message.chat.id, 'Если хочешь оценить работу разработчика!\nСсылка: https://forms.gle/AKAFG747aYGydynm7')
        # Сюда можете ввести свою ссылку на Телеграмм, тогда пользователя будет перекидывать к вам в личку
        webbrowser.open("https://forms.gle/AKAFG747aYGydynm7")
    elif message.text == '⚙️ Тг канал разработчика':
        # Функционал, чтобы пользователи следили за новостями разработчика
        bot.send_message(message.chat.id, 'Хочешь следить за новостями разработчика в его телеграмм канале?:\nСсылка: https://t.me/logneosome')

        # Сюда можете ввести свою ссылку на Телеграмм, тогда пользователя будет перекидывать к вам в личку
        webbrowser.open_new_tab("https://t.me/logneosome")
    elif message.text == '💳 Купить' or message.text == '✏️ Написать разработчику!\nСсылка:https://t.me/neosome ':
        webbrowser
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    # Если пользователь написал свое сообщение, то бот рандомно генерирует один из возможных вариантов ответа
    # Добавлять и редактировать варианты ответов можно в списке answers
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])

# Функция, отвечающая за раздел товаров
def goodsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🍯 Липовый мед')
    button2 = types.KeyboardButton('🍯 Цветочный мед')
    button3 = types.KeyboardButton('🍯 Сотовый мед')
    button4 = types.KeyboardButton('🍯 Настойка восковой моли')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)

# Функция, отвечающая за раздел настроек
def settingsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('⚙️ Отзыв')
    button2 = types.KeyboardButton('⚙️ Тг канал разработчика')
    button3 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Раздел настроек.\nВыбери один из вариантов:', reply_markup=markup)

# Функция, отвечающая за раздел помощи
def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1)
    bot.send_message(message.chat.id, 'Раздел справки.\nЗдесь ты можешь написать моему разработчику.\nСсылка: https://t.me/neosome', reply_markup=markup)

# Строчка, чтобы программа не останавливалась
bot.polling(none_stop=True)
