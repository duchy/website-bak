#!/usr/bin/env python
#coding=utf-8

import Image,ImageDraw,ImageFont,os,string,random,ImageFilter 
import chardet
import time

class picChecker:
	""" 
	usage: pc = picChecker().createChecker() 
	param: 很多，如下 
		outputType 输出类型 
			类型 string 
			默认值 GIF 
			可选值 GIF JPEG TIFF PNG 
		mode 图片模式 
			类型 string 
			可选值 RGB L (还有其他模式，但只推荐这2种) 
			默认值 RGB 
		backgroundColor 背景色 
		foregroundColor 前景色 
			当mode=RGB时，backgroundColor,foregroundColor为tutle类型 
			取值为(integer,integer,integer) 
			表示RGB颜色值 
			当mode=L时，backgroundColor,foregroundColor为数字，表示黑白模式 
			取值为0-255 
			表示灰度 
	return: [char count, image address] 
	""" 
	def __init__(self,size = (440,2048),fontsize = 18, 
				begin = (5,-2),outputType = 'PNG',mode = 'RGB' , 
				backgroundColor = (255,255,255), foregroundColor = (0, 0, 0), 
				fonttype = "ae_AlArabiya.ttf",length = 5,jamNum = (1,2), 
				pointBorder = (40,39)): 
		""" 
		初始化配置 
		""" 
		#图片大小 
		self.size = size 
		#字符起始插入点 
		self.begin = begin 
		#字符串长度 
		self.length = length 
		#输出类型 
		self.outputType = outputType 
		#字符大小 
		self.fontsize = fontsize 
		self.defaultfontsize = 14 
		#图片模式 
		self.mode = mode 
		#背景色 
		self.backgroundColor = backgroundColor 
		#前景色 
		self.foregroundColor = foregroundColor 

		#字体库路径 
		#self.fonttype = fonttype 
		self.fonttype ="fonts/wqy-zenhei/wqy-zenhei.ttc"
		self.defaultfonttype ="fonts/wqy-zenhei/wqy-zenhei.ttc"
		#self.fonttype ="fonts/wqy-microhei/wqy-microhei.ttc"
		#self.fonttype ="fonts/wqy-bitmapsong/wenquanyi_12pt.pcf"

		#设置字体,大小默认为18 
		self.font = ImageFont.truetype(self.fonttype, self.fontsize)
		self.defaultfont = ImageFont.truetype(self.defaultfonttype, self.defaultfontsize)
		
		self.borderSize = 10
		self.outlineSize = 2
		self.alignment = (0,0)
		self.borderColor = (40, 40, 40)
		self.textSize = (200, 100)
	
	def createChecker(self, text): 
		""" 
		usage: createChecker() 
		return: [str,pic] 
		str:对应的字符串 
		pic:对应的图片 
		for: 
		todo: 
		""" 
#		tcharset = chardet.detect(text[0:10])['encoding']
		tcharset = "utf8"
		self.size = (440, self.font.getsize(u'0')[1])
		#randStr = self.getPicString() + u'(The End)'
		randStr = text.decode(tcharset) + u'\n\n———— THE END ————\n  http://eqbaobei.com/cgi-bin/txt2pic.cgi 文字转图片\n'
		srctxt = randStr
		length=len(srctxt)
		txtlinewidth = self.size[0] - self.borderSize * 2
		txtlineheight = self.size[1]
		i = 0
		endj = 0
		lines = 0;
		tl=()
		summary=""
		while i < length:
		    tmpSize=self.font.getsize(srctxt[i:i+1])
		    oldtmpSize=tmpSize
		    for j in range(i + 1, length + 1):
			if srctxt[j - 1] == u'\n':
			    endj = j
		            break
		        oldtmpSize=tmpSize
			tmpSize = self.font.getsize(srctxt[i:j])
			if tmpSize[0] > txtlinewidth:
			    j -= 1
			    endj = j
			    break

			if tmpSize[0] == txtlinewidth:
			    oldtmpSize = tmpSize
			    endj = j
			    if j < length  and ( srctxt[j] == u' ' or srctxt[j] == u' '):
			        j += 1
			    break
		    #print i, j
		    tl += ((i, endj, ) + oldtmpSize + (lines, ), )
		    i = j
		    lines += 1
		height = lines * self.size[1] + 2 * self.borderSize
		self.size = (self.size[0], height)
		im = Image.new(self.mode,self.size,self.borderColor)
		draw = ImageDraw.Draw(im) 

		outline = (self.outlineSize, self.outlineSize, im.size[0]-self.outlineSize - 1, im.size[1]-self.outlineSize - 1)
		draw.rectangle(outline, fill=self.backgroundColor)
		
		for lo in tl: 
		    #print lo
		    currfont = self.font
		    destxt = srctxt[lo[0]:lo[1]]
		    if lo[4] == lines - 1:
		        currfont = self.defaultfont
		        #x = int((im.size[0] - currfont.getsize(destxt)[0] - self.borderSize * 2) + self.borderSize + 0.5)
		        x = int((im.size[0] - currfont.getsize(destxt)[0] - self.borderSize * 2) * self.alignment[0] / 2 + self.borderSize + 0.5)
		    elif lo[4] == lines - 2:
		        currfont = self.defaultfont
		        x = int((im.size[0] - currfont.getsize(destxt)[0] - self.borderSize * 2) * 1 / 2 + self.borderSize + 0.5)
		    elif lo[4] == 0:
			summary=srctxt[lo[0]:lo[1]]
		        x = int((im.size[0] - lo[2] - self.borderSize * 2) * 1 / 2 + self.borderSize + 0.5)
		    else:
		        x = int((im.size[0] - lo[2] - self.borderSize * 2) * self.alignment[0] / 2 + self.borderSize + 0.5)
		    y = int((im.size[1] - lo[3] - self.borderSize * 2) * self.alignment[1] / 2 + self.borderSize + txtlineheight * lo[4] + 0.5)
		    #print x, y, destxt
	            draw.text((x,y), destxt, font=currfont, fill=self.foregroundColor)

		ctime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
		pngpath ="images/t2p/" + ctime  + ".png" 
		im.save("../" + pngpath, self.outputType)
		#print randStr
		return {'title':summary.encode("utf8"), 'length':length-68, 'imgaddr':pngpath}
