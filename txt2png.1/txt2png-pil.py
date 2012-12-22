# -*- coding: utf-8 -*-

import os
import Image, ImageFont, ImageDraw

text = u"这是一段测试文本，test 123。"

im = Image.new("RGB", (300, 50), (255, 255, 255))
dr = ImageDraw.Draw(im)
#font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)
fontpath=os.path.join("fonts","wqy-zenhei", "wqy-zenhei.ttc")
font = ImageFont.truetype(fontpath, 18)

dr.text((10, 5), text, font=font, fill="#000000")

im.show()
im.save("t.png")
