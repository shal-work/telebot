import telebot
from telebot import types

# import react
# import keyframes
# import wordpress
# import vue
# import php
# import charts
# import document
# import landing

import config, img_const, react, keyframes, wordpress, vue, php, charts, document, landing


bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text1 = '🇷🇺 Привет, '
    text2 = 'Здесь можно посмотреть мои наработки по разработке сайтов!'
    name = message.from_user.first_name if message.from_user.first_name else "Незнакомец"
    markup_inline = types.InlineKeyboardMarkup()
    btn_in_1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/repository/')
    btn_in_2 = types.InlineKeyboardButton('Подробнее', callback_data='Abou_btn')
    markup_inline.row(btn_in_1, btn_in_2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_1 = types.KeyboardButton('🇷🇺 ✋ Об авторе')
    markup.add(btn_1)
    text = text1 + ' ' + name + '!'
    try:
        bot.send_photo(message.chat.id, img_const.start, caption=text, parse_mode="HTML", reply_markup=markup)
    except:
        with open(img_const.empty, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup)
    bot.send_message(message.chat.id,  text2, parse_mode="HTML", reply_markup=markup_inline)


@bot.message_handler(commands=['help'])
def help(message):
    text1 = 'Для того чтобы получить интересующую тебя информацию просто нажми на любую из этих команд, отправь их вручную или выбери из списка доступных команд в специальном меню'
    text2 = '<b>Команды11:</b>'
    text3 = '/start - Перезапустить бота'
    text4 = '/website - Список сайтов'
    text5 = '/help - Помощь'
    bot.send_message(message.chat.id, text1 + '\n' + text2 + '\n'+ text3 +'\n' + text4 +'\n' + text5, parse_mode="HTML")


@bot.callback_query_handler(func=lambda callback: callback.data == 'Abou_btn')
def callback_msg(callback):
    message = callback.message
    # if callback.data == 'Abou_btn':
        # bot.send_message(callback.message.chat.id, "Эта опция пока находтися в разработке")

    markup_inline = types.InlineKeyboardMarkup()
    btn_in_React = types.InlineKeyboardButton('React', callback_data='React_btn') #1
    btn_in_Keyframes = types.InlineKeyboardButton('Keyframes', callback_data='Keyframes_btn') #2
    btn_in_WordPress = types.InlineKeyboardButton('WordPress', callback_data='WordPress_btn') #3
    btn_in_Vue = types.InlineKeyboardButton('Vue', callback_data='Vue_btn')
    btn_in_PHP = types.InlineKeyboardButton('PHP', callback_data='PHP_btn')
    btn_in_Charts = types.InlineKeyboardButton('Графики', callback_data='Charts_btn')
    btn_in_Document = types.InlineKeyboardButton('Документ', callback_data='Document_btn')
    btn_in_Landing = types.InlineKeyboardButton('Лендинги', callback_data='Landing_btn')

    markup_inline.row(btn_in_React, btn_in_Keyframes)
    markup_inline.row(btn_in_WordPress, btn_in_Vue)
    markup_inline.row(btn_in_PHP, btn_in_Charts)
    markup_inline.row(btn_in_Document, btn_in_Landing)
    bot.send_message(message.chat.id, '<b>Подробнее:</b>', parse_mode="HTML", reply_markup=markup_inline)


landing.register_commands(bot)#8
document.register_commands(bot)#7
charts.register_commands(bot)#6
php.register_commands(bot)#5
vue.register_commands(bot)#4
wordpress.register_commands(bot) #3
keyframes.register_commands(bot) #2
react.register_commands(bot) #1



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '🇷🇺 ✋ Об авторе':
        text = ' 🇷🇺 Просто - увлечение. Прошел курсы по практике разработки HTML / CSS, BOOTSTRAP , PHP / MySQL, Linux / GIT, CodeIgniter, JavaScript / jQuery, WordPress. Изучаю Vue, React, TypeScript-React. Результат выкладываю на GitHub, ссылка https://shal-work.github.io/repository/. Все нельзя запомнить, но можно найти ответы в интернете, главное знать как этим воспользоваться!'
        # with open('./img/About_AlekseyHtml_bot.jpg', 'rb') as photo:
        try:
            bot.send_photo(message.chat.id, img_const.about, caption=text, parse_mode="HTML")
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML")



@bot.message_handler(content_types='text')
def send_text(message):
    bot.send_message(message.chat.id, message)
    if message.text=="React":
        bot.send_message(message.chat.id, "Это")

bot.infinity_polling()
