# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:24:20 2022

@author: Burcu Özdemir
"""
Pip Install pyqrcode

import pyqrcode

from PIL import Image
link = input("Enter anything to generate QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRcode.png")