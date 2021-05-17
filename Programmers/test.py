import requests
import re
import bs4
import urllib.request
url = 'https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko'
response = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(response,'html.parser')
# print(soup)
result = soup.find_all('article',{'class':'MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne'})

print(result[0])
count = 1
# for i in result:
#     print(i)
#     print('\n\n\n')
#     print(count,'뉴스',i.text)
#     print('\n\n\n')
#     count += 1
