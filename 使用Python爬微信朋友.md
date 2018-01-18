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

