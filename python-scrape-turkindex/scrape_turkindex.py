from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as soup
import os.path

# sayfa 1
my_url = 'http://www.turkindex.com/index.asp?CID=1219&pg=1&uid=3'

# sayfa 2
# my_url = 'http://www.turkindex.com/index.asp?CID=1219&pg=2&uid=3'

# sayfa 3
# my_url = 'http://www.turkindex.com/index.asp?CID=1219&pg=3&uid=3'

# Opening up connection and grabbing the page
uClient = uRequest(my_url)

# assign the content to a variable
page_html = uClient.read()

# close the connection
uClient.close()

page_html = page_html.decode('ISO-8859-9')

# page_html=re.sub('</font>','',page_html)
# page_html=re.sub('<br />','',page_html)

page_html = page_html.replace('</font>','')
page_html = page_html.replace('<br />','')

# html parsing
page_soup = soup(page_html, 'html.parser')

market_tables = page_soup.findAll('table', attrs={'class':'siyah_10', 'cellpadding':'3'})

filename = 'markets.csv'
file_exists = os.path.isfile(filename)
f = open(filename,'a')
headers = 'market_name, address, city\n'
if not file_exists:
	f.write(headers)

for market_table in market_tables:
	market_name_with_numbers = market_table.find('b').text.strip()
	market_name = market_name_with_numbers[market_name_with_numbers.find('-'):].replace('-','')
	market_name = market_name.strip()
	city = market_table.find('font').select('b:nth-of-type(1)')[1].text.strip()
	address = market_table.find('font',{'color':'#333333'}).find(text=True, recursive=False).replace("\r", "").replace("\n", "")
	# print(address)
	print(market_name)
	f.write(market_name + ',' + address.replace(',', '') + ',' + city + '\n')

f.close()