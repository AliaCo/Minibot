import telebot
import wget
import minibot_token
import model as md

user_photos_path='/home/alcohan/Documents/MiniBot/userphoto/'
storage_photos_path='/home/alcohan/Documents/MiniBot/userphoto/photos/'
photo_to_send='file_3.jpg'

userStep = {} 
# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        print("User, who hasn't used \"/wanttosendbotphoto\" but send photo anyway")
        return 0

bot = telebot.TeleBot(minibot_token.token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	name = message.from_user.first_name
	bot.reply_to(message, f"Hi, {name}! I'm an echo bot 🙋 I echo everything you say.")

@bot.message_handler(commands=['wanttosendbotphoto'])
def send_message(message):
	cid = message.chat.id
	bot.reply_to(message, "Great! Than send me the photo NOW! Sorry, no presure, I'm waiting for you photo.")
	userStep[cid] = 1 

@bot.message_handler(content_types=['photo'], func=lambda message: get_user_step(message.chat.id) == 1)
def get_foto(message):
    users_photos = [i.file_id for i in message.photo]
    for n, i in enumerate(users_photos):
        user_file = bot.get_file(i)
        user_file_path = user_file.file_path
        downloaded_file = bot.download_file(user_file_path)
        with open(f'{user_photos_path}{user_file_path}', 'wb') as new_file:
            new_file.write(downloaded_file)
    bot.reply_to(message, "Tnx! Now I have you photos 😈.")
    userStep[message.chat.id] = 0 # reset the users step back to 0

@bot.message_handler(commands=['wanttogetphoto'])
def send_photo(message):
    bloha = md.EdsrModel()
    print(bloha.result())
    cid = message.chat.id
    bot.send_message(chat_id=cid, text=bloha.result())
	# bot.send_photo(chat_id=cid, photo=open(f'{storage_photos_path}{photo_to_send}', 'rb'))

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()
