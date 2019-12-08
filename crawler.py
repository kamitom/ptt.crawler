
import ssl
import bs4

import urllib.request as req

# 抓取 ptt NBA html

# 處理: urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:852)>
ssl._create_default_https_context = ssl._create_unverified_context

pttNBAurl = "https://www.ptt.cc/bbs/NBA/index6495.html"
# pttNBAurl = "https://www.ptt.cc/bbs/NBA/index.html"
# 建立一個request 物件,附加 headers 資訊
request = req.Request(pttNBAurl, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})

with req.urlopen(request) as response:
    pttNBAData = response.read().decode("utf-8")
# print(pttMovieData)

# 解析 pttMovieData 原始碼,取得每篇標題
root = bs4.BeautifulSoup(pttNBAData, "html.parser")
print(root.title.string)
# print(root)
# one_mvtitles = root.find("div", class_="title") # 只取其一
# print(one_mvtitles.a.string)
allNBAtitles = root.find_all("div", class_="title")
# print(allNBAtitles)
for title in allNBAtitles:
    if title.a != None:
        print(title.a.string)
