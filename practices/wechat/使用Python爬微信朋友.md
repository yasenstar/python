# itchat包的准备

Python里的itchat包，包含了wechat的个人账户API接口，用其来爬取个人微信信息进行本地分析非常方便。

首先，在终端安装一下itchat包

```
pip install itchat
```

安装完成后导入包，再登陆自己的微信。过程中会产生一个登陆二维码，扫描之后即可登陆。登陆成功后可以把登陆的微信账号的好友相关信息爬下来。

```python
import itchat
itchat.login()
# 爬取自己好友相关信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]
```

有了上面的friends数据，就可以来做分析了。

# 自己微信好友的男女比例

仔细观察返回的数据结构，发现“性别”是存放在一个字典中的，key是"sex"，男性值是1，女性值是2，其他事不明性别的（就是没有填的）。

可以通过下面的循环获取想要的性别数据，得到自己微信好友的性别比例。

```python
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
```

出来的结果可以调用R来做出好看的图表。

# 自己微信好友的城市分布

作为准备，安装pandas

```
pip install pandas
```

再仔细观察friends列表，发现里面还包含了好友昵称、省份、城市、个人简介等等的数据，可以用来分析好友城市发布，最好的方式是定义一个函数来把数据都爬下来，存到数据框中，再进行分析。如下：

```python
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
```

以上会得到一个叫data.csv的文件，用R打开并简单做一下数据预处理，就可以作图了。

# 自己微信好友的个人签名

作为准备，安装jieba

```
pip install jieba
```

打印出好友的个性签名(Signature)，对于某些表情等等无关词汇，需要先替换掉，另外，还有类似<>/=之类的符号，也需要用正则替换掉，再把所有结果拼起来，得到text字符串

```python
import re
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1fd+w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
```

使用jieba分词：

```python
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)
```

---
感谢[alfred](http://mp.weixin.qq.com/s/mW7PTofuCOQrW5e34Ei2Pw)
