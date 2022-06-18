from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'

# Opening up connection and grabbing the page
uClient = uRequest(my_url)

# assign the content to a variable
page_html = uClient.read()

# close the connection
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')

# grabs each product
containers = page_soup.findAll('div', {'class':'item-container'})

filename = 'products.csv'
f = open(filename,'w')
headers = 'brand, product_name, shipping\n'
f.write(headers)

for container in containers:
	brand = container.find('div','item-info').div.img['title']
	title_container = container.findAll('a',{'class':'item-title'})
	product_name = title_container[0].text
	shipping_container = container.findAll('li',{'class':'price-ship'})
	shipping_price = shipping_container[0].text.strip()

	print("Brand: " + brand)
	print("Product Name: " + product_name)
	print("Shipping Price: " + shipping_price)

	f.write(brand + ',' + product_name.replace(',', '-') + ',' + shipping_price + '\n')

f.close()