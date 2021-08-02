import urllib.request
r = urllib.request.urlopen("http://placekitten.com/200/300")
image = r.read()

with open('cat.jpg','wb') as f:
    f.write(image)
