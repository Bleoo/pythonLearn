import re
import urllib.request

from pip._vendor import requests

SAVE_DIR_PATH = '/Users/bleoo/Desktop/urlpull/'
save = lambda url: open(SAVE_DIR_PATH + url[url.rfind('/') + 1:], 'wb').write(requests.get(url).content)

url = 'https://www.zhihu.com/question/36462611?utm_medium=social&utm_source=qq'
req = urllib.request.Request(url, headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
oper = urllib.request.urlopen(req)
data = oper.read().decode('UTF-8')
linkre = re.compile('src="(https://pic.+?\.jpg)"')

for x in linkre.findall(data):
    print('图片 --->  ' + x)
    save(x)
