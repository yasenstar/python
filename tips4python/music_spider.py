import bs4
import requests
# 搜索函数
def searchdownload(name):
    # 从网站的Requests Header中获取
    url = 'https://music.hwkxk.cn/?kw=%s&lx=wy' % name
    html = requests.get(url=url).text
    html = html.encode('ISO-8859-1')
    html = html.decode('UTF-8')
    # 解析网页
    soup = bs4.BeautifulSoup(html, "lxml")
    # 查找目标
    link_0 = soup.select('.btn-success')
    print(link_0)