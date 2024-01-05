from telebot import types
import img_const

def register_commands(bot):
    @bot.callback_query_handler(func=lambda callback: callback.data == 'Vue_btn')
    def callback_msg(callback):
        id = callback.message.chat.id
        text1 = '<b>Сайты на Vue</b>'
        text2 = '/scooter - самокат для Яндекс Go'
        text3 = '/table- Cделать таблицу с сортировкой'
        text4 = '/restaurent- Переписал сайт на Vue 3.0'
        text = text1 + '\n' + text2 +'\n' + text3 +'\n' + text4
        markup_inline = types.InlineKeyboardMarkup()
        btn_in = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in)
        bot.send_message(id, text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['scooter'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/scooter/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/scooter')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Сделать верстку по аналогии сайта https://go.yandex/ru_ru/lp/rides/scooter/'
        try:
            bot.send_photo(message.chat.id, img_const.scooter, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['table'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/table-vue3.0/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/table-vue3.0')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Задание: сделать таблицу с сортировкой'
        try:
            bot.send_photo(message.chat.id, img_const.table, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['restaurent'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/homepage_restaurent_paralax/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/homepage_restaurent_paralax')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Переписал сайт на Vue 3.0'
        try:
            bot.send_photo(message.chat.id, img_const.parallax, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)
