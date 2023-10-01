from tqdm.auto import tqdm
from super_image import EdsrModel, ImageLoader
from PIL import Image
import requests
import torch
from io import BytesIO

url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class Model:
    def __init__(self):
        self.model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=4)
        self.model = self.model.to(device)

    def predict(self, path):
        print('Prediction starts')
        self.image = Image.open(path)
        self.image = ImageLoader.load_image(self.image).to(device)

        self.preds = self.model(self.image)
        ImageLoader.save_image(self.preds, '/home/alcohan/Documents/MiniBot/result/scaled_4x.png')
        self.result = '/home/alcohan/Documents/MiniBot/result/scaled_4x.png'
        print('Prediction ready')
        return self.result
