from telebot import types
import img_const

def register_commands(bot):
    @bot.callback_query_handler(func=lambda callback: callback.data == 'Charts_btn')
    def callback_msg(callback):
        id = callback.message.chat.id
        text1 = '<b>Сайты c графиками на canvas</b>'
        text2 = '/biorhythm - биоритмы'
        text3 = '/studik - задание для студика'
        text = text1 + '\n' + text2 +'\n' + text3
        markup_inline = types.InlineKeyboardMarkup()
        btn_in = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in)
        bot.send_message(id, text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['biorhythm'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/biorhythm/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/biorhythm')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Самая первая программа - биоритмы'
        try:
            bot.send_photo(message.chat.id, img_const.biorhythm, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['studik'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/studik/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/studik')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Переписал сайт на Vue 3.0'
        try:
            bot.send_photo(message.chat.id, img_const.studik, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)
