from tqdm.auto import tqdm
from super_image import EdsrModel, ImageLoader
from PIL import Image
import requests
import torch
from io import BytesIO

url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# path = "/kaggle/input/someface/IMG_20230814_194712_169.jpg"

class Model:
    def __init__(self):
        self.model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=4)
        self.model = self.model.to(device)

    def predict(self):
        self.image = Image.open(requests.get(url, stream=True).raw)
        self.image = ImageLoader.load_image(self.image).to(device)

        self.preds = self.model(self.image)
        ImageLoader.save_image(self.preds, '/home/alcohan/Documents/MiniBot/result/scaled_4x.png')
        self.result = '/home/alcohan/Documents/MiniBot/result/scaled_4x.png'
        return self.result

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# image = Image.open(path)

# model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=4) # scale 2, 3 and 4 models available
# model = model.to(device)
# inputs = ImageLoader.load_image(image)
# inputs = inputs.to(device)
# preds = model(inputs)