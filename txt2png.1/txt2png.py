# -*- coding: utf-8 -*-

import os
import StringIO
import Image, ImageFont, ImageDraw
import pygame

pygame.init()

text=u"这只是一个测试程序。。。great....sucess!"

im = Image.new("RGB", (300, 100), (255, 255, 255))
fontpath=os.path.join("fonts","wqy-zenhei", "wqy-zenhei.ttc")
font = pygame.font.Font(fontpath, 18)

rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))

sio = StringIO.StringIO()
pygame.image.save(rtext, sio)
sio.seek(0)

line = Image.open(sio)
im.paste(line, (10, 5))

im.save("t.png")
