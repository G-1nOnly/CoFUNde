import urllib.request
import urllib.error

r = urllib.request.Request("http:www.baidu.com")
try:
    urllib.request.urlopen(r)
except urllib.error.URLError as e:
    print(e.reason)

R = urllib.request.Request\
    ("https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/texlive2018.iso")
#404 not found

try:
    urllib.request.urlopen(R)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e)
