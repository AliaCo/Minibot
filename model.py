from tqdm.auto import tqdm
from super_image import EdsrModel, ImageLoader
from PIL import Image
import requests
import torch

url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
# path = "/kaggle/input/someface/IMG_20230814_194712_169.jpg"

class EdsrModel:
    def __init__(self) -> None:
        pass

    def predict():
        result = 'Hey, Im working:)'
        return result

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# image = Image.open(path)

# model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=4) # scale 2, 3 and 4 models available
# model = model.to(device)
# inputs = ImageLoader.load_image(image)
# inputs = inputs.to(device)
# preds = model(inputs)

import model as md
    cid = message.chat.id
    bot.send_message(chat_id=cid, text=bloha.result())