import urllib.request
url = "https://www.baidu.com/"
proxy_support = urllib.request.ProxyHandler({'http':'120.239.73.65'})
#代理设置
opener = urllib.request.build_opener(proxy_support) #创建opener
urllib.request.install_opener(opener)#安装opener

r = urllib.request.urlopen(url)
html = r.read().decode('UTF-8')
print(html)