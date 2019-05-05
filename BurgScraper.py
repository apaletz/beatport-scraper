import csv
import urllib2
import time
from bs4 import BeautifulSoup as soup
hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

burg_list_url = "https://burgerweek.co/halifax-burger-week-lineup-2019/"

burg_response = urllib2.urlopen(burg_list_url)

burg_html = burg_response.read()

burger_soup = soup(burg_html)

containers = burger_soup.findAll("article", {"class":"mix portfolio_category_141 portfolio_category_127 portfolio_category_138 portfolio_category_139 portfolio_category_133 portfolio_category_137  mix_all show"})

names = burger_soup.findAll("h2", {"class":"portfolio_title"})

succes_count = 0

#to get ontly the text use name[i].a.text

#make list to hold names
just_names = []

for name in names:
	just_names.append(name.a.text)

# for element in just_names:
# 	print(element)
#open the link from burger_soup based on contents, then grab price

links = burger_soup.findAll("a", {"class":"portfolio_link_for_touch" })

restau_urls = []


for link in links:
	restau_urls.append(link.get('href'))

# for item in restau_urls:
# 	print(item)

#test with item[0]


restau_list = []

with open('burgers.csv', 'wb') as burg_csv:
	filewriter = csv.writer(burg_csv, delimiter=',')

	for x in range(len(restau_urls)):

		try:

			test_response = urllib2.urlopen(restau_urls[x])
			test_html = test_response.read()
			test_soup = soup(test_html)
			box = test_soup.find("div",{"class":"wpb_wrapper"})

			try:
				restau_name = box.find("div", {"class":"burgerlineup"}).p.text
			except:
				try:
					restau_name = box.find("h4").text
				except:
					restau_name = "restaurant name not scraped"
			
			
			try:
				addy = box.findAll("span")
				addy = addy[2].text
			except:
				try:
					addy = box.find("div",{"class":"address"}).div.p.text
				except:
					addy = "address not scraped"


			try:
				burg_name = box.find("div",{"class":"burgerlineup"}).div.h2.span.text
			except:
				try:
					burg_name = box.find("div",{"class":"wpb_wrapper"}).p.text
				except:
					burg_name = "name not scraped"
			
			try:
				price = box.find("div",{"class":"wpb_text_column wpb_content_element burgprice"}).div.h1.text
			except:
				try:
					price = box.find("div",{"class":"wpb_text_column wpb_content_element burgprice"}).div.p.text
				except:
					price = "price not scraped"
			
			description = box.find("div",{"class":"wpb_text_column wpb_content_element"}).p.text

			print("successful scrape")
			
			succes_count+=1

			filewriter.writerow([restau_name.encode("utf-8"), addy.encode("utf-8"), burg_name.encode("utf-8"), price.encode("utf-8"), description.encode("utf-8")])

			time.sleep(5)

		except:

			print("connection error")

			filewriter.writerow([" connection".encode("utf-8"), "error".encode("utf-8"), "unable".encode("utf-8"), "to".encode("utf-8"), "get data".encode("utf-8")])

			time.sleep(5)


	print("succesful scrapes " + str(succes_count))





