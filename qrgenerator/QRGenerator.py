#!/usr/bin/python3

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
        eps_file_location = str(self.__file_location__)+'.eps'
        png_file_location = str(self.__file_location__)+'.png'
        print('url eps:'+eps_file_location)
        print('url eps:'+png_file_location)
        url = pyqrcode.create(self.__crypt_text__)
        print('paso 1:' )
        url.eps(eps_file_location, scale=10)
        print('paso 2:')
        target_bounds = (2080, 2080)
        print('paso 3:')
        pic = Image.open(eps_file_location)
        print('paso 4:')
        pic.load(scale=10)
        print('paso 5:')
        if pic.mode in ('P', '1'):
            pic = pic.convert("RGB")
        print('paso 6:')
        ratio = min(target_bounds[0] / pic.size[0],
                    target_bounds[1] / pic.size[1])
        print('paso 7:')
        new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))
        print('paso 8:')
        # Resize to fit the target size
        pic = pic.resize(new_size, Image.ANTIALIAS)
        print('paso 9:')
        draw = ImageDraw.Draw(pic)
        print('paso 10:')
        font = ImageFont.truetype("/opt/wildfly/standalone/data/python/ModuloQR/qrgenerator/OpenSans-Bold.ttf", 60)
        print('paso 11:')
        lines = self.__qr_code__.splitlines()
        print('paso 12:')
        w = font.getsize(max(lines, key=lambda s: len(s)))[0]
        print('paso 13:')
        x, y = pic.size
        x /= 2
        x -= w / 2
        y = y - 100
        print('paso 14:')
        draw.text((x, y), self.__qr_code__, font=font, fill="Black")
        print('paso 15:')
        pic.save(png_file_location)
