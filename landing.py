from telebot import types
import img_const

def register_commands(bot):
    @bot.callback_query_handler(func=lambda callback: callback.data == 'Landing_btn')
    def callback_msg(callback):
        id = callback.message.chat.id
        text1 = '<b>Лендинги по аналогичным из WordPress, то что понравилось!</b>'
        text2 = '/bakery - Лендинг пекарни'
        text3 = '/restaurent1 - Лендинг ресторана'
        text4 = '/restaurent2 - Лендинг ресторана'
        text5 = '/ceramic - Лендинг студии керамики'
        text6 = '/construction - Лендинг реконструкции'
        text7 = '/hotel - Лендинг отеля'
        text = text1 + '\n' + text2 + '\n' + text3 + '\n' + text4+ '\n' + text5+ '\n' + text6+ '\n' + text7
        markup_inline = types.InlineKeyboardMarkup()
        btn_in = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in)
        bot.send_message(id, text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['bakery'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/bakery/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/bakery')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Своя верстка по образцу, образец лендинг из WordPress'
        try:
            bot.send_photo(message.chat.id, img_const.bakery, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['restaurent1'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/restaurent/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/restaurent')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Своя верстка по образцу, образец лендинг из WordPress'
        try:
            bot.send_photo(message.chat.id, img_const.restaurent1, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['restaurent2'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/homepage_restaurent/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/homepage_restaurent')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Своя верстка по образцу, образец лендинг из WordPress'
        try:
            bot.send_photo(message.chat.id, img_const.restaurent2, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['hotel'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/lending_hotel/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/lending_hotel')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Своя верстка по образцу, образец лендинг из WordPress'
        try:
            bot.send_photo(message.chat.id, img_const.hotel, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['construction'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/under_construction/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/under_construction')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Своя верстка по образцу, образец лендинг из WordPress'
        try:
            bot.send_photo(message.chat.id, img_const.construction, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['construction'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/under_construction/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/under_construction')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Своя верстка по образцу, образец лендинг из WordPress'
        try:
            bot.send_photo(message.chat.id, img_const.construction, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)
