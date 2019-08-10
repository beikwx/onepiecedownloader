import urllib.request
import re
import os

# 定义集数，从前面到后面-1
books = list(range(950, 952))

for book in books:
    # https://one-piece.cn/post/10922/
    url = "https://one-piece.cn/post/10" + str(book) + "/"
    date = urllib.request.urlopen(url).read().decode("utf-8")
    # src="http://wx3.sinaimg.cn/large/83940082gy1fwdhpmdqezj20nm0y6gvw.jpg"
    os.mkdir("D:\\Desktop\\image\\" + str(book))
    pat = 'src="(http:\\S+.jpg)"'
    img_urls = re.compile(pat).findall(date)
    print("当前下载" + str(book) + "集")
    count = 1
    for img_url in img_urls[0:-1]:
        print("正在下载" + img_url + str(count))
        output_name = "D:\\Desktop\\image\\" + str(book) + "\\" + str(count) + ".jpg"
        urllib.request.urlretrieve(img_url, output_name)
        count += 1
