import telebot
import wget
import minibot_token
import model as md

user_storage_path='/home/alcohan/Documents/MiniBot/userphoto/'
storage_photos_path='/home/alcohan/Documents/MiniBot/userphoto/photos/'
photo_to_send='file_3.jpg'

userStep = {}
userPhoto = {}
# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        print("User, who hasn't used \"/wanttosendbotphoto\" but send photo anyway")
        return 0
    
def get_user_photo(uid):
     if uid in userPhoto:
          return userPhoto[uid]
     else:
          print('User hasn\'t uploaded photo yet.')
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
    ur_photos = [i.file_id for i in message.photo]
    ur_ph_file = bot.get_file(ur_photos[-1]) # take only high resolution photo from list
    ur_ph_file_pth = ur_ph_file.file_path
    downloaded_file = bot.download_file(ur_ph_file_pth)
    with open(f'{user_storage_path}{ur_ph_file_pth}', 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Tnx! Now I have you photo 😈.")
    userStep[message.chat.id] = 0 # reset the users step back to 0
    userPhoto[message.chat.id] = f'{user_storage_path}{ur_ph_file_pth}' # add path to the users photo to dict

@bot.message_handler(commands=['wanttogetphoto'])
def send_photo(message):
    cid = message.chat.id
    if get_user_photo(message.chat.id) == 0:
        bot.send_message(chat_id=cid, text='Please, upload photo using "wanttosendbotphoto" command first.')
    else:
        bloha = md.Model()
        pred = bloha.predict(get_user_photo(message.chat.id))
        print(pred)
        bot.send_photo(chat_id=cid, photo=open(pred, 'rb'))

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()
