import telebot
import wget
import minibot_token

user_photos_path='/home/alcohan/Documents/MiniBot/userphoto/'
storage_photos_path='/home/alcohan/Documents/MiniBot/userphoto/photos/'
photo_to_send='file_3.jpg'

bot = telebot.TeleBot(minibot_token.token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	name = message.from_user.first_name
	bot.reply_to(message, f"Hi, {name}! I'm an echo bot 🙋 I echo everything you say.")

@bot.message_handler(commands=['wanttosendbotphoto'])
def send_message(message):
	bot.reply_to(message, "Great! Than send me the photo NOW! Sorry, no presure, I'm waiting for you photo.")

@bot.message_handler(content_types=['photo'])
def get_foto(message):
    users_photos = [i.file_id for i in message.photo]
    for n, i in enumerate(users_photos):
        user_file = bot.get_file(i)
        user_file_path = user_file.file_path
        downloaded_file = bot.download_file(user_file_path)
        with open(f'{user_photos_path}{user_file_path}', 'wb') as new_file:
            new_file.write(downloaded_file)
    bot.reply_to(message, "Tnx! Now I have you photos 😈.")

@bot.message_handler(commands=['wanttogetphoto'])
def send_photo(message):
	chat_id = message.chat.id
	bot.send_photo(chat_id=chat_id, photo=open(f'{storage_photos_path}{photo_to_send}', 'rb'))

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()
