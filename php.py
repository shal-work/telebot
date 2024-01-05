from telebot import types
import img_const

def register_commands(bot):
    @bot.callback_query_handler(func=lambda callback: callback.data == 'PHP_btn')
    def callback_msg(callback):
        id = callback.message.chat.id
        text1 = '<b>Сайт на PHP </b>'
        text2 = '/codeigniter - сайт MVC на CodeIgniter/PHP'
        text = text1 + '\n' + text2
        markup_inline = types.InlineKeyboardMarkup()
        btn_in_3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in_3)
        bot.send_message(id, text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['codeigniter'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='http://z91117el.beget.tech/decision/show/item.php')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin3)
        text = 'Cайт MVC на CodeIgniter/PHP'
        try:
            bot.send_photo(message.chat.id, img_const.codeigniter, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)
