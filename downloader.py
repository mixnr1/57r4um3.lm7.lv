import time
import requests
from bs4 import BeautifulSoup
from lxml import html

start = time.time()
start_tuple=time.localtime()
start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_tuple)

url='https://straume.lmt.lv/lv/video-saraksts/tutas-lietas'

page=requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
mydivs = soup.find_all("a", {"class": "video-title"})
# print(len(mydivs))
# print(mydivs[1])
# print(type(mydivs[1]))
# print(dir(mydivs[1]))
# print(mydivs[1].attrs["href"])

all_url=[]
for i in range(0,len(mydivs)):
    #  print(mydivs[i])#single video
     all_url.append('https://straume.lmt.lv'+mydivs[i].attrs["href"])
print(all_url)

    

end = time.time()
end_tuple = time.localtime()
end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_tuple)
print("Script ended: "+end_time)
print("Script running time: "+time.strftime('%H:%M:%S', time.gmtime(end - start)))