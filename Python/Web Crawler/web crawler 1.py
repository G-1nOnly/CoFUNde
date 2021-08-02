#爬虫
import urllib.request
r = urllib.request.urlopen("http://www.baidu.com")
#URL:  protocol :// hostname[:port] / path / [;parameters][?query]#fragment
html = r.read() #read()函数读取文件
html = html.decode("UTF-8") #以UTF-8解码 encode则将str转为2进制数据
print(html)

req = urllib.request.Request("http://www.baidu.com/")
response = urllib.request.urlopen(req)
print(response.geturl())
print(response.info())  #服务器返回信息