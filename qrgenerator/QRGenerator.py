#!/usr/bin/python3
import os

import pyqrcode
from PIL import Image, ImageDraw, ImageFont


class QRGeneratorLogic:
    __file_location__ = ''
    __crypt_text__ = ''
    __qr_code__ = ''

    def __init__(self, file_location, qr_code, crypt_text):
        self.__file_location__ = file_location
        self.__qr_code__ = qr_code
        self.__crypt_text__ = crypt_text

    def generate_qr_code(self):
        eps_file_location = str(self.__file_location__)+'.png'
        url = pyqrcode.create(self.__crypt_text__)
        url.png(eps_file_location, scale=10)
        # Guardar EPS
        pic = Image.open(eps_file_location)
        if pic.mode in ('P', '1'):
            pic = pic.convert("RGB")
        # Resize to fit the target size
        pic = Image.open(eps_file_location)
        draw = ImageDraw.Draw(pic)
        font = ImageFont.truetype(str(os.path.dirname(os.path.abspath(__file__))) + "/OpenSans-Bold.ttf", 60)
        lines = self.__qr_code__.splitlines()
        w = font.getsize(max(lines, key=lambda s: len(s)))[0]
        x, y = pic.size
        x /= 2
        x -= w / 2
        y = y - 100
        draw.text((x, y), self.__qr_code__, font=font, fill="Black")
        pic.save(eps_file_location)
