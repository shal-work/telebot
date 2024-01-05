from telebot import types
import img_const

def register_commands(bot):
    @bot.callback_query_handler(func=lambda callback: callback.data == 'Document_btn')
    def callback_msg(callback):
        id = callback.message.chat.id
        text1 = '<b>Сайты для просмотра документа</b>'
        text2 = '/document - Сайт для тренировки с data-атрибутами и обработки их на js'
        text = text1 + '\n' + text2
        markup_inline = types.InlineKeyboardMarkup()
        btn_in = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in)
        bot.send_message(id, text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['document'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/fishing/')
        btn2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/fishing')
        btn3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn1, btn2)
        markup_inline.add(btn3)
        text = 'Сайт показывает документ и при клике на гиперссылку отображает участки карты'
        try:
            bot.send_photo(message.chat.id, img_const.document, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)
