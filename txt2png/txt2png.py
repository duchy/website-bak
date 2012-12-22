#coding=utf-8
import Image,ImageDraw,ImageFont,os,string,random,ImageFilter 
def initChars(): 
	""" 
	允许的字符集合，初始集合为数字、大小写字母 
	usage: initChars() 
	param: None 
	return: list 
	返回允许的字符集和 
	for: picChecker类初始字符集合 
	todo: Nothing 
	""" 
	nums = [str(i) for i in range(10)] 
	letterCase = [ 
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 
	'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 
	'w', 'x', 'y'
	] 
	upperCase = [ 
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 
	'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
	'W', 'X', 'Y'
	] 
	return(nums+letterCase+upperCase)
	
class picChecker:
	""" 
	图片验证代码： 
	1) 用户注册需填写图片验证码，以阻止机器人注册 
	2) 图片验证码字符数为 4 位(大小写字母与数字，不区分大小写)。 
	用户如果没有填写验证码或没有填写正确的验证码， 
	页面友好性提示用户填写(同时程序方面也做相应限制) 
	usage: pc = picChecker().createChecker() 
	param: 很多，如下 
		chars 允许的字符集合， 
			类型 list 
			默认值 initChars() 
			例子 ['1','2','3'] 
		length 字符串长度 
			类型 integer 
			默认值 4 
		size 图片大小 
			类型 tutle 
			默认值 (120,30) 
			例子 (120,30) 
		fontsize 字体大小 
			类型 integer 
			默认值 25 
		begin 字符其实位置，即左上角位置 
			类型 tutle 
			默认值 (5,-2) 
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
		fonttype 字体路径 
			类型 string 
			默认值 "simsum.ttc" 
		jamNum 干扰线条数 
			类型 (int1,int1) 
			int1 干扰线条数下限，包含 
			int2 干扰线条数上线，包含 
		pointBorder 散点噪音 
			构造方法：对每个像素点使用随机函数确定是否在该像素上画散点噪音 
			类型 (int1,int2) 
			int1越大 散点越多 
			int2越大 散点越少 
	return: [picCheckerStr,pic] 
	picCheckerStr: 表示返回图片中对应的字符串,可用于session验证以及其他用途 
	pic : 返回的图片，类型为Image 
	for : 
	todo : Nothing 
	""" 
	#默认字体路径 
	#DEFAULT_FONT_PATH = os.path.join(os.path.dirname(__file__),'simsun.ttc').replace('\\','/') 
	def __init__(self,chars = initChars(),size = (440,2048),fontsize = 18, 
				begin = (5,-2),outputType = 'PNG',mode = 'RGB' , 
				backgroundColor = (255,255,255), foregroundColor = (0, 0, 0), 
				fonttype = "ae_AlArabiya.ttf",length = 5,jamNum = (1,2), 
				pointBorder = (40,39)): 
		""" 
		初始化配置 
		""" 
		#验证码配置 
		#允许的字符串 
		self.chars = chars 
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
		#图片模式 
		self.mode = mode 
		#背景色 
		self.backgroundColor = backgroundColor 
		#前景色 
		self.foregroundColor = foregroundColor 
		#干扰线条数 
		self.jamNum = jamNum 
		#散点噪音界限 
		self.pointBorder = pointBorder 
		#字体库路径 
		self.fonttype = fonttype 
		self.fonttype ="fonts/wqy-zenhei/wqy-zenhei.ttc"
		#self.fonttype ="fonts/wqy-microhei/wqy-microhei.ttc"
		#self.fonttype ="fonts/wqy-bitmapsong/wenquanyi_12pt.pcf"

		#设置字体,大小默认为18 
		self.font = ImageFont.truetype(self.fonttype, self.fontsize)
		
		self.borderSize = 10
		self.outlineSize = 2
		self.alignment = (0,0)
		self.borderColor = (40, 40, 40)
		self.textSize = (200, 100)
	
	def getPicString(self): 
		""" 
		usage: getPicString() 
		return: string 
		for : 生成给定长度的随机字符串 
		todo: Nothing 
		""" 
		#初始化字符串长度 
		length = self.length 
		#初始化字符集合 
		chars = self.chars 
		#获得字符集合 
		selectedChars = random.sample(chars,length) 
		charsToStr = string.join(selectedChars,'') 
		return u"""荷塘月色
　　朱自清
　　这几天心里颇不宁静。今晚在院子里坐着乘凉，忽然想起日日走过的荷塘，在这  朱自清满月的光里，总该另有一 番样子吧。月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；妻在屋里拍着闰儿（1），迷迷糊糊地哼着眠歌。我悄悄地披了大衫，带上门出去。
　　沿着荷塘，是一条曲折的小煤屑路。这是一条幽僻的路；白天也少人走，夜晚更加寂寞。荷塘四周，长着许多树，蓊蓊（wěng）郁郁（2）的。路的一旁，是些杨柳，和一些不知道名字的树。没有月光的晚上，这路上阴森森的，有些怕人。今晚却很好，虽然月光也还是淡淡的。
　　路上只我一个人，背着手踱（duó）着。这一片天地好像是我的；我也像超出了平常的自己，到了另一个世界里。我爱热闹，也爱宁静；爱群居，也爱独处。像今晚上，一个人在这苍茫的月下，什么都可以想，什么都可以不想，便觉是个自由的人。白天里一定要做的事，一定要说的话，现在都可不理。这是独处的妙处，我且受用这无边的荷香月色好了。
　　曲曲折折的荷塘上面，弥望（3）的是田田（4）的叶子。叶子出水很高，像亭亭的舞女的裙。层层的叶子中间，零星地点缀着些白花，有袅娜（niǎo,nuó）（5）地开着的，有羞涩地打着朵儿的；正如一粒粒的明珠，又如碧天里的星星，又如刚出浴的美人。微风过处，送来缕缕清香，仿佛远处高楼上渺茫的歌声似的。这时候叶子与花也有一丝的颤动，像闪电般，霎时传过荷塘的那边去了。叶子本是肩并肩密密地挨着，这便宛然（6）有了一道凝碧的波痕。叶子底下是脉脉（mò）（7）的流水，遮住了，不能见一些颜色；而叶子却更见风致（8）了。
　　月光如流水一般，静静地泻在这一片叶子和花上。薄薄的青雾浮起在荷塘里。叶子和花仿佛在牛乳中洗过一样；又像笼着轻纱的梦。虽然是满月，天上却有一层淡淡的云，所以不能朗照；但我以为这恰是到了好处——酣眠固不可少，小睡也别有风味的。月光是隔了树照过来的，高处丛生的灌木，落下参差斑驳（9）的黑影，峭楞楞如鬼一般；弯弯的杨柳的稀疏的倩影（10），却又像是画在荷叶上。塘中的月色并不均匀；但光与影有着和谐的旋律，如梵婀玲（11）上奏着的名曲。
　　荷塘的四面，远远近近，高高低低都是树，而杨柳最多。这些树将一片荷塘重重围住；只在小路一旁，漏着几段空隙，像是特为月光留下的。树色一例（12）是阴阴的，乍看像一团烟雾；但杨柳的丰姿（13），便在烟雾里也辨得出。树梢上隐隐约约的是一带远山，只有些大意罢了。树缝里也漏着一两点路灯光，没精打采的，是渴睡人的眼。这时候最热闹的，要数树上的蝉声与水里的蛙声；但热闹是它们的，我什么也没有。
　　忽然想起采莲的事情来了。采莲是江南的旧俗，似乎很早就有，而六朝时为盛；从诗歌里可以约略知道。采莲的是少年的女子，她们是荡着小船，唱着艳歌（14）去的。采莲人不用说很多，还有看采莲的人。那是一个热闹的季节，也是一个风流（15）的季节。梁元帝（16）《采莲赋》里说得好：
　　于是妖童媛（yuán）女，荡舟心许（17）；鷁（yì）首（18）徐回，兼传羽杯；櫂（zhào）（19）将移而藻挂，船欲动而萍开。尔其纤腰束素，迁延顾步；夏始春余，叶嫩花初，恐沾裳而浅笑，畏倾船而敛裾(jū)（20）。
　　可见当时嬉游的光景了。这真是有趣的事，可惜我们现在早已无福消受了。
　　于是又记起，《西洲曲》（21）里的句子：
　　采莲南塘秋，莲花过人头；低头弄莲子，莲子清如水。
　　今晚若有采莲人，这儿的莲花也算得“过人头”了；只不见一些流水的影子，是不行的。这令我到底惦着江南了。——这样想着，猛一抬头，不觉已是自己的门前；轻轻地推门进去，什么声息也没有了，妻已睡熟好久了。
		"""
	
	def createChecker(self): 
		""" 
		usage: createChecker() 
		return: [str,pic] 
		str:对应的字符串 
		pic:对应的图片 
		for: 
		todo: 
		""" 
		self.size = (440, self.font.getsize(u'0')[1])
		randStr = self.getPicString() + u'(The End)'
		srctxt = randStr
		length=len(srctxt)
		txtlinewidth = self.size[0] - self.borderSize * 2
		txtlineheight = self.size[1]
		i = 0
		lines = 0;
		tl=()

		while i < length:
		    for j in range(i, length):
			if srctxt[j] == u'\n':
		            break
			tmpSize = self.font.getsize(srctxt[i:j])
			if tmpSize[0] >= txtlinewidth and j < length and srctxt[j+1] != u'\n':
			    #print tmpSize, "size of this line"
			    j-=2
			    break
		    #print i, j
		    tl += ((i, j + 1, ) + tmpSize + (lines, ), )
		    i = j + 1
		    lines += 1
		height = lines * self.size[1] + 2 * self.borderSize
		self.size = (self.size[0], height)
		im = Image.new(self.mode,self.size,self.borderColor)
		draw = ImageDraw.Draw(im) 

		outline = (self.outlineSize, self.outlineSize, im.size[0]-self.outlineSize, im.size[1]-self.outlineSize)
		draw.rectangle(outline, fill=self.backgroundColor)
		
		for lo in tl: 
		    #print lo
		    destxt = srctxt[lo[0]:lo[1]]
		    if lo[4] == lines - 1:
		        x = int((im.size[0] - lo[2] - self.borderSize * 2) + self.borderSize + 0.5)
		    elif lo[4] == 0:
		        x = int((im.size[0] - lo[2] - self.borderSize * 2) * 1 / 2 + self.borderSize + 0.5)
		    else:
		        x = int((im.size[0] - lo[2] - self.borderSize * 2) * self.alignment[0] / 2 + self.borderSize + 0.5)
		    y = int((im.size[1] - lo[3] - self.borderSize * 2) * self.alignment[1] / 2 + self.borderSize + txtlineheight * lo[4] + 0.5)
		    #print x, y, destxt
	            draw.text((x,y), destxt, font=self.font, fill=self.foregroundColor)

		im.save("t2p.png",self.outputType)
		#print randStr
		return [randStr,im]
		
if __name__ == '__main__': 
	#c=picChecker(foregroundColor=(82, 124, 178)) 
	c=picChecker(foregroundColor=(12, 54, 108)) 
	t=c.createChecker() 
	print "Done."
