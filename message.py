
"""
reated on Fri Dec 28 13:58:04 2018

@author: takano.hiroyuki
"""


import random
import urllib.request
from bs4 import BeautifulSoup

def getAllMessage():
    url = u"http://fuita.net/hitokoto/sort/point/1"

    html = urllib.request.urlopen(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    res = []
    for li in soup.find_all('li'):
        #res.append(li.text)
        #res.append(li.text.split("\n")[2])
        try:
            wk = li.text
            wk = wk.split("\n")[2]
            res.append(wk)
        except:
            print("")
    return res

def returnMessage(msglist):
    total = len(msglist)
    num = random.uniform(1, total)
    num = int(num)
    msg = msglist[num]

    return msg

if __name__ == "__main__":
    msglist = getAllMessage()
    myword = returnMessage(msglist)
    print(myword)

~
