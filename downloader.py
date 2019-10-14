import time
import requests
from bs4 import BeautifulSoup
import config
import re

start = time.time()
start_tuple=time.localtime()
start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_tuple)

url='https://straume.lmt.lv/lv/video-saraksts/tutas-lietas'

page=requests.get(url, proxies=config.proxies, allow_redirects=False)
soup = BeautifulSoup(page.content, 'html.parser')
mydivs = soup.find_all("a", {"class": "video-title"})
all_url=[]
for i in range(0,len(mydivs)):
     all_url.append('https://straume.lmt.lv'+mydivs[i].attrs["href"])
# all_mp4=[]
file_text=open("links.txt",'w')
for mp4 in all_url:
    page=requests.get(mp4, proxies=config.proxies, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    mymp4 = soup.find_all('script')
    for script in mymp4:
        if re.findall('/tvinet.lmt.lv/+.+mp4', str(script)):
            # print(re.findall('/tvinet.lmt.lv/+.+mp4', str(script)))
            # all_mp4.append(re.findall('/tvinet.lmt.lv/+.+mp4', str(script)))
            file_text.write(str(re.findall('/tvinet.lmt.lv/+.+mp4', str(script))).split("'")[1] + '\n')
file_text.close()
   

end = time.time()
end_tuple = time.localtime()
end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_tuple)
print("Script ended: "+end_time)
print("Script running time: "+time.strftime('%H:%M:%S', time.gmtime(end - start)))