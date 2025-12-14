import asyncio
import telebot as tb
bot = tb.TeleBot('8587227790:AAEGDlDFm10YXPiGpBliNdi8QYqKV3Y3iLw')
from telebot import types
user_state = []
user_status = []
chat_id = None
text_send = None
time_message_minute = None
time_message_hour = None
time_message_day = None
time_message_week = None
is_msg_send = None
time_message = None
async def main(x):
    await x
@bot.message_handler(commands=['start'])
def bot_start(message):
    with open(r'Привет(файл бота не удалять).jpg', 'rb') as hi:
        bot.send_photo(message.from_user.id,hi, 'Приветствую вас, я бот для отправки сообщений, вот вам краткий гайд по коммандам!\n/msg - позволяет отправить сообщение через опредленное время.\nНапоминаем это ещё ранняя версия этого бота, он будет дорабатываться и неоднакратно, оставить отзыв и пожелания /review\n/guide - гайд по использованию бота. ')
@bot.message_handler(commands=['msg'], content_types=['text'])
def msg(message):
    global user_state
    user_state = ['msg']
    if user_state == ['msg']:
        if user_status == ['ord']:
            pass
        else:
            with open(r'Написать читото(файл бота, не удалять).jpg', 'rb') as KIRA:
                bot.send_photo(message.from_user.id, KIRA, 'Добро пожаловать в мой основной функционал, вот список доступных вам комманд и их описание.\n/sm (send minute) - Отправить сообщение в указанный вами чат через заданное вами количество минут. (Не может превышать лимит: 7200 - 5 дней)\n/sh (send hour) - Отправить сообщение в указанный вами чат, через указанное вами количество часов.(не может превышать: 120 - 5 дней)\n/sd (send day) - Отправить сообщение в указанный вами чат, через определенный день. (не может превышать: 5 - 5 дней)')
            @bot.message_handler(commands=['sm'], content_types=['text'])
            def send_minute(message):
                global user_state
                if user_state == ['msg']:
                    def sid(message):
                        global chat_id
                        chat_id = message.text
                        bot.send_message(message.from_user.id, 'Пожалуйста, введите Текст сообщения которое вы хотите отправить:')
                        bot.register_next_step_handler(message, stt)
                    def stt(message): #send_text
                        global text_send, chat_id
                        text_send = message.text
                        bot.send_message(message.from_user.id, 'Укажите, через сколько минут, вы хотите отправить сообщение')
                        bot.register_next_step_handler(message, st)
                    def st(message): #send_time
                        global time_message_minute
                        time_message_minute = int(message.text)
                        bot.send_message(message.from_user.id, 'Ожидайте сообщения в указанный вами чат')
                        asyncio.run(main(send_msg()))
                    async def send_msg():
                        global time_message_minute, time_message, chat_id, text_send, is_msg_send
                        time_message = time_message_minute * 60
                        if time_message > 432000:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение более чем на 5 дней вперед.')
                        elif time_message < 0:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение в прошлое.')
                        else:
                            await asyncio.sleep(time_message)
                            bot.send_message(chat_id, text_send)
                            is_msg_send = True
                            msg_gg()
                    def msg_gg():
                        global is_msg_send, time_message_minute, chat_id, text_send, time_message
                        if is_msg_send == True:
                            time_message_minute = None
                            chat_id = None
                            text_send = None
                            is_msg_send = None
                            time_message = None
                    bot.send_message(message.from_user.id, 'Пожалуйста, введите цифровой ID чата (Как получить цифровой ID /id), в который вы хотите отправить сообщение:')
                    bot.register_next_step_handler(message, sid)
            @bot.message_handler(commands=['sh'], content_types=['text'])
            def send_hour(message):
                global user_state, chat_id, text_send, time_message_hour, time_message_minute, time_message, is_msg_send
                if user_state == ['msg']:
                    def sid(message):
                        global chat_id
                        chat_id = message.text
                        bot.send_message(message.from_user.id, 'Введите сообщение которое вы хотите отправить в этот чат')
                        bot.register_next_step_handler(message, stt)
                    def stt(message):
                        global text_send
                        text_send = message.text
                        bot.send_message(message.from_user.id, 'Укажите через сколько часов вы хотите отправить сообщение')
                        bot.register_next_step_handler(message, st)
                    def st(message):
                        global time_message_hour
                        time_message_hour = int(message.text)
                        if time_message_hour > 120:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение более чем на 5 дней вперед.')
                        elif time_message_hour < 0:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение в прошлое.')
                        else:
                            bot.send_message(message.from_user.id, 'Укажите через сколько минут вы хотите отправить сообщение:')
                            bot.register_next_step_handler(message, stm)
                    def stm(message): #set_time_minute
                        global time_message_minute
                        time_message_minute = int(message.text)
                        asyncio.run(main(send_msg()))
                    async def send_msg():
                        global time_message_minute, chat_id, text_send, is_msg_send, time_message
                        time_message = (time_message_hour * 3600) + (time_message_minute * 60)
                        if time_message > 432000:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение более чем на 5 дней вперед.')
                        elif time_message < 0:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение в прошлое.')
                        else:
                            await asyncio.sleep(time_message)
                            bot.send_message(chat_id, text_send)
                            is_msg_send = True
                            msg_gg()
                    def msg_gg():
                        global user_state, chat_id, text_send, time_message_hour, time_message_minute, time_message, is_msg_send
                        if is_msg_send == True:
                            time_message_minute = None
                            chat_id = None
                            text_send = None
                            is_msg_send = None
                            time_message = None
                            time_message_hour = None
                    bot.send_message(message.from_user.id, 'Пожалуйста, введите цифровой ID чата (Как получить цифровой ID /id) ,в который вы хотите отправить сообщение ()')
                    bot.register_next_step_handler(message, sid)
            @bot.message_handler(commands=['sd'], content_types=['text'])
            def send_day(message):
                if user_state == ['msg']:
                    def sid(message):
                        global chat_id
                        chat_id = message.text
                        bot.send_message(message.from_user.id, 'Отправьте текст сообщения которое вы хотите отправить:')
                        bot.register_next_step_handler(message, stt)
                    def stt(message):
                        global text_send
                        text_send = message.text
                        bot.send_message(message.from_user.id, 'Укажите через сколько дней вы хотите отправить сообщение')
                        bot.register_next_step_handler(message, sd)
                    def sd(message):
                        global time_message_day
                        time_message_day = int(message.text)
                        if time_message_day > 5:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение более чем на 5 дней вперед.')
                        elif time_message_day < 0:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение в прошлое.')
                        else:
                            bot.send_message(message.from_user.id, 'Укажите через сколько часов вы хотите отправить сообщение')
                            bot.register_next_step_handler(message, sh)
                    def sh(message):
                        global time_message_hour, time_message_day
                        time_message_hour = int(message.text)
                        th = (time_message_day * 24) + time_message_hour
                        if th > 120:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение более чем на 5 дней вперед.')
                        elif th < 0:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение в прошлое.')
                        else:
                            bot.send_message(message.from_user.id, 'Укажите через сколько минут вы хотите отправить сообщение')
                            bot.register_next_step_handler(message, sm)
                    def sm(message):
                        global time_message_day, time_message_hour, time_message_minute, time_message
                        time_message_minute = int(message.text)
                        asyncio.run(main(send_msg()))
                    async def send_msg():
                        global time_message_minute, chat_id, text_send, is_msg_send, time_message, time_message_day
                        time_message = (time_message_day*86400)+(time_message_hour * 3600) + (time_message_minute * 60) 
                        if time_message > 432000:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение более чем на 5 дней вперед.')
                        elif time_message < 0:
                            bot.send_message(message.from_user.id, 'Вы не можете отправить сообщение в прошлое.')
                        else:
                            await asyncio.sleep(time_message)
                            bot.send_message(chat_id, text_send)
                            is_msg_send = True
                            msg_gg()
                    def msg_gg():
                        global user_state, chat_id, text_send, time_message_hour, time_message_minute, time_message, is_msg_send
                        if is_msg_send == True:
                            time_message_minute = None
                            chat_id = None
                            text_send = None
                            is_msg_send = None
                            time_message = None
                            time_message_hour = None
                bot.send_message(message.from_user.id, 'Пожалуйста, отправьте цифровой ID чата (Как получить цифровой ID /id), в который вы хотите отправить сообщение:')
                bot.register_next_step_handler(message,sid)
@bot.message_handler(commands=['review'], content_types = ['text'])
def rew(message):
    def rewuwer(message):
        us_text = message.text
        bot.send_message(-1003325379834, us_text)
        us_text = None
    bot.send_message(message.from_user.id, 'Отправьте отзыв или пожелание связанные с ботом, они будут учитываться в следующем обновлении:')
    bot.register_next_step_handler(message, rewuwer)
@bot.message_handler(commands=['guide'])
def guide(message):
    with open(r'На помощь(файл бота не удалять).jpg', 'rb') as Help:
        bot.send_photo(message.from_user.id, Help, 'Выберите, что именно вызвало у вас вопрос:\n/id - Как получить нужный для бота ID.\n/time - как нужно указывать время.\n/question - Задать вопрос связанный с ботом, но не указанный здесь.')
@bot.message_handler(commands=['id'])
def id_que(message):
    bot.send_message(message.from_user.id, 'У вас вызвало вопрос, как найти необходимый для бота ID.\nДля получения вашего ID или ID вашего друга откройте @getmy_idbot, нажмите START и вам отправят ваш цифровой ID.\nДля получения ID друга так же активируйте @getmy_idbot и введите его юзернэйм, после чего вам отправят его числовой ID.\nДля получения ID телеграм каналов отправьте ссылку на выбранный вами канал или перешлите от туда сообщение. (Так же в @getmy_idbot)')
@bot.message_handler(commands=['time'])
def time_que(message):
    bot.send_message(message.from_user.id, 'У вас вызвало вопрос, как именно нужно указывать временной промежуток.\nВписывайте число, оно будет отправлено через тот промежуток времени который вам отправил бот.\n При указывании времени если суммарно получится отрицательное значение, бот не будет отправлять ваше сообщение, Т.К сообщение буквально никак нельзя отправить в прошлое.\nВ данной версии бота доступен лимит до 5 дней, не более, если суммарно время через которое вы хотите отправить сообщение будет превышать данный лимит, то сообщение не будет отправлено.')
@bot.message_handler(commands=['question'])
def question_que(message):
    global user_id
    def step2():
        user_id = message.from_user.id
        us_text = message.text
        bot.send_message(-1003325379834, us_text + ' ' + str(user_id))
        us_text = None
        user_id = None
    bot.send_message(message.from_user.id, 'Задавайте вопрос на который вы не нашли в /guide.')
    bot.register_next_step_handler(message, step2)
bot.polling(non_stop=False, interval=0,timeout=0)