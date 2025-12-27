import itchat
itchat.login()

# 爬取自己好友相关信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器
male = famale = other = 0
# friends[0]是自己的信息，所以要从friend[1]开始
for i in friends[1:]:
	sex = i["Sex"]
	if sex == 1:
		male += 1
	elif sex == 2:
		famale += 1
	else:
		other += 1

# 计算朋友总数
total = len(friends[1:])

# 打印出自己的好友性别比例
print ("男性好友：  %.2f%%" % (float(male)/total*100) + "" + "女性好友：  %.2f%%" % (float(famale)/total*100) + "" + "不明性别好友：  %.2f%%" % (float(other)/total*100))

# 定义一个函数，用来爬取各个变量
def get_var(var):
	variable = []
	for i in friends:
		value = i[var]
		variable.append(value)
	return variable

# 调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var("NickName")
Sex = get_var("Sex")
Province = get_var("Province")
City = get_var("City")
Signature = get_var("Signature")
from pandas import DataFrame
data = {"NickName": NickName, "Sex": Sex, "Province": Province, "City": City, "Signature": Signature}
frame = DataFrame(data)
frame.to_csv("data.csv", index=True)

import re
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1fd+w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)

import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)