from telebot import types
import img_const


def register_commands(bot):
    @bot.callback_query_handler(func=lambda callback: callback.data == 'Keyframes_btn')
    def callback_msg(callback):
        id = callback.message.chat.id
        # text1 = '<b>Тренировка с <tg-spoiler>@keyframes </tg-spoiler></b>'
        text1 = '<b>Тренировка с <code>@keyframes</code></b>'
        text2 = '/moidodyr - Мойдодыр'
        text3 = '/livehat - Живая шляпа'
        text4 = '/hedgehog - Ёжик в тумане'
        text5 = '/kolobok - Колобок'
        text6 = '/helios - helios'
        text7 = '/sborkademo - Аналог helios'
        text8 = '/moskvich - Москвич'
        markup_inline = types.InlineKeyboardMarkup()
        btn_in_3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btn_in_3)
        text = text1 + '\n' + text2 + '\n'+ text3 +'\n' + text4 +'\n' + text5 +'\n' + text6 +'\n' + text7 +'\n' + text8
        bot.send_message(id, text, parse_mode="HTML", reply_markup=markup_inline)


    @bot.message_handler(commands=['moidodyr'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/moidodyr/')
        btnin2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/moidodyr')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin2)
        markup_inline.add(btnin3)
        # with open (img_const.moidodyr, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='<b>Тренировка</b> <code>@keyframes</code>', parse_mode="HTML",  reply_markup=markup_inline )
        text = '<b>Тренировка</b> <code>@keyframes</code>'
        try:
            bot.send_photo(message.chat.id, img_const.moidodyr, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['livehat'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/livehat/')
        btnin2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/livehat')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin2)
        markup_inline.add(btnin3)
        # with open (img_const.livehat, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Тренировка с <code>@keyframes</code>', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Тренировка с <code>@keyframes</code>'
        try:
            bot.send_photo(message.chat.id, img_const.livehat, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['hedgehog'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/hedgehog/')
        btnin2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/hedgehog')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin2)
        markup_inline.add(btnin3)
        # with open (img_const.hedgehog, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Тренировка с <code>@keyframes</code>', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Тренировка с <code>@keyframes</code>'
        try:
            bot.send_photo(message.chat.id, img_const.hedgehog, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['kolobok'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/kolobok/')
        btnin2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/kolobok')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin2)
        markup_inline.add(btnin3)
        # with open (img_const.kolobok, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Тренировка с <code>@keyframes</code>', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Тренировка с <code>@keyframes</code>'
        try:
            bot.send_photo(message.chat.id, img_const.kolobok, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['helios'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/sborkademo_master/')
        btnin2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/sborkademo_master')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin2)
        markup_inline.add(btnin3)
        # with open (img_const.helios, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Сделал верстку как <code>http://helios.sborkademo.com</code>', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Сделал верстку как <code>http://helios.sborkademo.com</code>'
        try:
            bot.send_photo(message.chat.id, img_const.helios, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['sborkademo'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/sborkademo/')
        btnin2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/sborkademo')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin2)
        markup_inline.add(btnin3)
        # with open (img_const.sborkademo, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Сделал свою верстку по образцу <code>http://helios.sborkademo.com</code>', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Сделал свою верстку по образцу <code>http://helios.sborkademo.com</code>'
        try:
            bot.send_photo(message.chat.id, img_const.sborkademo, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)

    @bot.message_handler(commands=['moskvich'])
    def keyfr(message):
        markup_inline = types.InlineKeyboardMarkup()
        btnin1 = types.InlineKeyboardButton('Перейти на сайт', url='https://shal-work.github.io/moskvich/')
        btnin2 = types.InlineKeyboardButton('На GitHub', url='https://github.com/shal-work/moskvich')
        btnin3 = types.InlineKeyboardButton('🔙 Назад', callback_data='delete')
        markup_inline.add(btnin1, btnin2)
        markup_inline.add(btnin3)
        # with open (img_const.moskvich, 'rb') as photo:
        #     bot.send_photo(message.chat.id, photo, caption='Сделал свою верстку по образцу <code>https://nissan-evolution.ru</code>', parse_mode="HTML", reply_markup=markup_inline)
        text = 'Сделал свою верстку по образцу <code>https://nissan-evolution.ru</code>'
        try:
            bot.send_photo(message.chat.id, img_const.moskvich, caption=text, parse_mode="HTML", reply_markup=markup_inline)
        except:
            with open(img_const.empty, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup_inline)
