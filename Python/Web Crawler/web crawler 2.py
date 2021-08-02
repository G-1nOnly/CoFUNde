import urllib.request,urllib.parse
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

head = {} #通过表单隐藏自己
head['User-Agent'] ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
            'AppleWebKit/537.36 (KHTML, like Gecko) ' \
            'Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'

data = {}  #网站上获得
data['i']='anarchy'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data['client'] = 'fanyideskweb'
data = urllib.parse.urlencode(data).encode('UTF-8')  #访问有道词典 现有sign与salt反爬虫

r = urllib.request.urlopen(url,data,head)
#也可以用 r.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
#            'AppleWebKit/537.36 (KHTML, like Gecko) ' \
#            'Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763') 来添加

html = r.read().decode('UTF-8')
print(html)
