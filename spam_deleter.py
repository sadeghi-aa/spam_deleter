from flask import Flask
from flask import request
import telebot

app = Flask(__name__)

token = "1854811438:AAGiriL0MQAGZsGHYzLvDs7AbkI829u3htM"
bot = telebot.TeleBot(token, threaded=False)

warning_text = '\n'.join([
    'پیامتون به خاطر رعایت نکردن قوانین پاک شد.',
    'لطفاً پیام پین‌شده رو مطالعه کنید.'])

@app.route('/', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=['del'])
def delete(message):
    chat_id = message.chat.id
    if chat_id < 0:
        user_id = message.from_user.id
        member = bot.get_chat_member(chat_id, user_id)
        if member.status != 'member':
            if message.reply_to_message:
                replied_to = bot.get_chat_member(chat_id, message.reply_to_message.from_user.id)
                if replied_to.status == 'member':
                    spam_id = message.reply_to_message.message_id
                    spammer_id = replied_to.user.id
                    spammer_name = message.reply_to_message.from_user.first_name
                    command_id = message.message_id
                    bot.delete_message(chat_id, spam_id)
                    bot.delete_message(chat_id, command_id)
                    mention = "[" + spammer_name + "](tg://user?id="+str(spammer_id)+")"
                    text = '\n'.join([mention, warning_text])
                    bot.send_message(chat_id, text, parse_mode="Markdown")
                else: # Tried to delete an admin's message
                    command_id = message.message_id
                    bot.delete_message(chat_id, command_id)
            else: # Not replied on anything
                command_id = message.message_id
                bot.delete_message(chat_id, command_id)
        else: # Not an admin
            command_id = message.message_id
            bot.delete_message(chat_id, command_id)
