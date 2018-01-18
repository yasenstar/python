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
