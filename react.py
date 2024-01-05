from telebot import types
import img_const

def register_commands(bot):
    @bot.callback_query_handler(func=lambda callback: callback.data == 'React_btn')
    def callback_msg(callback):
        id = callback.message.chat.id
        # bot.send_message(callback.message.chat.id, "Эта опция по React_btn")
        text1 = '<b>Сайты на React</b>'
        text2 = '/react1- Cайт для тестирования'
        text3 = '/react2- Cайт для тестирования на TypeScript '
        text4 = '/react3- Сайт описывающий алгоритм  создания проекта на React'
        text5 = '/react4- Лендинг на React'
        markup_inline = types.InlineKeyboardMarkup()
        btn_in_3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in_3)
        bot.send_message(id, text1 + '\n' + text2 + '\n'+ text3 +'\n' + text4 +'\n' + text5, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['react1'])
    def react(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn_in_1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/test')
        btn_in_2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/test')
        btn_in_3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in_1, btn_in_2)
        markup_inline.add(btn_in_3)
        # with open (img_const.react1, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Cайт для тестирования на React', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Cайт для тестирования на React'
        try:
            bot.send_photo(message.chat.id, img_const.react1, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)


    @bot.message_handler(commands=['react2'])
    def react(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn_in_1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/test-on-TypeScriptReact')
        btn_in_2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/test-on-TypeScriptReact')
        btn_in_3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in_1, btn_in_2)
        markup_inline.add(btn_in_3)
        # with open (img_const.react1, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Cайт для тестирования на TypeScriptReact', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Cайт для тестирования на TypeScriptReact'
        try:
            bot.send_photo(message.chat.id, img_const.react2, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)


    @bot.message_handler(commands=['react3'])
    def react(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn_in_1 = types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/shal-work/algorithm-on-React')
        btn_in_2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/algorithm-on-React')
        btn_in_3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in_1, btn_in_2)
        markup_inline.add(btn_in_3)
        # with open (img_const.react3, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Алгоритм создания сайта на React', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Алгоритм создания сайта на React'
        try:
            bot.send_photo(message.chat.id, img_const.react3, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)


    @bot.message_handler(commands=['react4'])
    def react(message):
        markup_inline = types.InlineKeyboardMarkup()
        btn_in_1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/test-task2/')
        btn_in_2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/test-task2')
        btn_in_3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in_1, btn_in_2)
        markup_inline.add(btn_in_3)
        text = 'Лендинг по заданию на React'
        try:
            bot.send_photo(message.chat.id, img_const.react4, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.callback_query_handler(func=lambda callback: True)
    def callback_msg(callback):
        if callback.data == 'delete':
            bot.delete_message(callback.message.chat.id, callback.message.message_id)
