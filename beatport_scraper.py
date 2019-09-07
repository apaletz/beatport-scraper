import pandas as pd
import csv
import urllib2
from bs4 import BeautifulSoup as soup 

#make list of all top 100 urls by genre

genre_urls=[
#afro-house
'https://www.beatport.com/genre/afro-house/89/top-100',
#bass house
'https://www.beatport.com/genre/bass-house/91/top-100',
#big room
'https://www.beatport.com/genre/big-room/79/top-100', 
#deep house
'https://www.beatport.com/genre/deep-house/12/top-100',
#dnb
'https://www.beatport.com/genre/drum-and-bass/1/top-100',
#dubstep
'https://www.beatport.com/genre/dubstep/18/top-100',
#dance
'https://www.beatport.com/genre/dance/39/top-100',
#electro house
'https://www.beatport.com/genre/electro-house/17/top-100',
#jackin' house
'https://www.beatport.com/genre/funky-groove-jackin-house/81/top-100',
#future house
'https://www.beatport.com/genre/future-house/65/top-100',
#garage
'https://www.beatport.com/genre/garage-bassline-grime/86/top-100',
#hard dance
'https://www.beatport.com/genre/hard-dance/8/top-100',
#hard techno
'https://www.beatport.com/genre/hardcore-hard-techno/2/top-100',
#house
'https://www.beatport.com/genre/house/5/top-100',
#nu-disco
'https://www.beatport.com/genre/indie-dance-nu-disco/37/top-100',
#progressive house
'https://www.beatport.com/genre/progressive-house/15/top-100',
#psy-trance
'https://www.beatport.com/genre/psy-trance/13/top-100',
#reggae/dancehall
'https://www.beatport.com/genre/reggae-dancehall-dub/41/top-100',
#tech house
'https://www.beatport.com/genre/tech-house/11/top-100',
#tehno
'https://www.beatport.com/genre/techno/6/top-100',
#trance
'https://www.beatport.com/genre/trance/7/top-100',
#trap/future bass
'https://www.beatport.com/genre/trap-future-bass/87/top-100']
#create csv file and make top row
#make a text file to hold all the links
track_links = open("TrackLinks.txt", "w")

#itterate through url list and scrape data for each url

for url in genre_urls:
	genre_response = urllib2.urlopen(url)
	genre_html = genre_response.read()
	genre_soup = soup(genre_html, features='html.parser')

	#make buckets out of each track's div
	buckets = genre_soup.findAll("li", {"class":"bucket-item ec-item track"})

	# genre = url.split('/')[4]

	# with open('all_genres.csv', 'wb') as all_genres_csv:
	# 	filewriter = csv.writer(all_genres_csv, delimiter=',')
	# 	filewriter.writerow('Artist', 'Title', 'Key', 'BPM', 'Genre')

	#make a text file of all the links


	for bucket in buckets:
		link = "https://www.beatport.com/" + bucket.find("p", {"class":'buk-track-title'}).a['href']

		track_links.write(link + "\n")

		# track_url = link

		# track_respone = urllib2.urlopen(link)

		# track_html = track_respone.read()

		# track_soup = soup(track_html, features="html.parser")

		# key = track_soup.find("li", {'class':"interior-track-content-item interior-track-key"}).span.findNext('span').text

		# # print(key)

		# bpm = track_soup.find("li", {'class':'interior-track-content-item interior-track-bpm'}).span.findNext('span').text

		# print(bpm)


		# genre = track_soup.find("li", {'class':"interior-track-content-item interior-track-genre"}).span.findNext('span').a.text
		
		# print(genre)

		# artist = bucket.find("p", {"class":"buk-track-artists"}).a.text

		# song_title = bucket.find("span", {"class":'buk-track-primary-title'}).text


		# print(artist + ": " + song_title +", " + key + ", " + bpm + " bpm" + " Genre: " + genre)

		# filewriter.writerow([artist.encode("utf-8"), song_title.encode("utf-8")
		# 	,key.encode("utf-8"), bpm.encode("utf-8"), genre.encode("utf-8")])

		# print(link)

		# track_url = link

		# track_respone = urllib2.urlopen(link)

		# track_html = track_respone.read()

		# track_soup = soup(track_html, features="html.parser")

		# key = track_soup.find("li", {'class':"interior-track-content-item interior-track-key"}).span.findNext('span').text

		# bpm = track_soup.find("li", {'class':'interior-track-content-item interior-track-bpm'}).span.findNext('span').text
		
		# artist = bucket.find("p", {"class":"buk-track-artists"}).a.text

		# song_title = bucket.find("span", {"class":'buk-track-primary-title'}).text

		# print(artist + ": " + song_title +", " + key + ", " + bpm + " bpm")

		# filewriter.writerow([artist.encode("utf-8"), song_title.encode("utf-8")
		# 	, key.encode("utf-8"), bpm.encode("utf-8")])

track_links.close()

# 	url_list = open("TrackLinks.txt").readlines()

# print(url_list)

# 	for url in url_list:
# 		track_url = url

# 		track_respone = urllib2.urlopen(track_url)

# 		track_html = track_respone.read()

# 		track_soup = soup(track_html, features="html.parser")

# 		key = track_soup.find("li", {'class':"interior-track-content-item interior-track-key"}).span.findNext('span').text

# 		# print(key)

# 		bpm = track_soup.find("li", {'class':'interior-track-content-item interior-track-bpm'}).span.findNext('span').text

# 		# print(bpm)


# 		genre = track_soup.find("li", {'class':"interior-track-content-item interior-track-genre"}).span.findNext('span').a.text
		
# 		# print(genre)

# 		artist = bucket.find("p", {"class":"buk-track-artists"}).a.text

# 		song_title = bucket.find("span", {"class":'buk-track-primary-title'}).text


# 		print(artist + ": " + song_title +", " + key + ", " + bpm + " bpm" + " Genre: " + genre)

		# filewriter.writerow([artist.encode("utf-8"), song_title.encode("utf-8")
		# 	,key.encode("utf-8"), bpm.encode("utf-8"), genre.encode("utf-8")])









