import itchat
import os
import math
import Image

# 登录微信
itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]

user = friends[0]["UserName"]

os.mkdir(user)

num = 0

# 下载微信头像
for i in friends:
	img = itchat.get_head_img(userName=i["UserName"])
	fileImage = open(user + "/" + str(num) + ".png","wb")
	fileImage.write(img)
	fileImage.close()
	num += 1

pics = os.listdir(user)

numPic = 400

print(f'照片数量:{numPic}')

eachsize = int(math.sqrt(float(640 * 640) / numPic))

print(f'每个照片的大小:{eachsize}')

numline = int(640 / eachsize)

print(f'每行照片数量:{numline}')

toImage = Image.new('RGBA', (640, 640))

x = 0
y = 0
n = 0

for i in pics:
	try:
		#打开图片
		img = Image.open(user + "/" + i)
	except IOError:
		pass
	else:
		#缩小图片
		img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * eachsize, y * eachsize))
		x += 1
		if x == numline:
			x =0
			y += 1
		n += 1
		#判断是否够400张图片
		if n == 400:
			break
