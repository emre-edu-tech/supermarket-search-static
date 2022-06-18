import requests
from bs4 import BeautifulSoup
s = requests.Session()
url='https://scanlibs.com/neural-networks-systems-evolutionary-algorithms-2nd/'
r=html=s.get(url).text
soup=BeautifulSoup(html,'html.parser')
relative_link=soup.find('a',{'id':'download'})['href'] #get the relative link
download_redirect_link=url+relative_link
headers={
"referer": url
}
r2=requests.get(download_redirect_link,headers=headers)
print(r2.url)