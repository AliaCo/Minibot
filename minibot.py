import telebot
import wget

token = "6332254442:AAFabS1P8QOWX_peDXU33MWZxJ68qNvbV4Y"

bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	name = message.from_user.first_name
	bot.reply_to(message, f"Hi, {name}! I'm an echo bot 🙋 I echo everything you say.")

@bot.message_handler(commands=['wanttosendbotphoto'])
def function_name(message):
	bot.reply_to(message, "Great! Than send me the photo NOW! Sorry, no presure, I'm waiting for you photo.")

@bot.message_handler(content_types=['photo'])
def function_name(message):
    users_photos = [i.file_id for i in message.photo]
    for n, i in enumerate(users_photos):
        user_file = bot.get_file(i)
        user_file_path = user_file.file_path
        downloaded_file = bot.download_file(user_file_path)
        with open(f'/home/alcohan/Documents/MiniBot/userphoto/{user_file_path}', 'wb') as new_file:
            new_file.write(downloaded_file)
    bot.reply_to(message, "Tnx! Now I have you photos 😈.")
	    # print('photo', i)
	    # print('file', user_file)
	    # print('file path', user_file_path)
# wget.download(f'https://api.telegram.org/file/bot{token}/{user_file_path}', '/home/alcohan/Documents/MiniBot/userphoto/')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()