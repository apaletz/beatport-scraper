import pandas as pd
import csv
import urllib2
from bs4 import BeautifulSoup as soup 

url_list = open("TrackLinks.txt").readlines()

# print(url_list)

with open('all_genres.csv', 'wb') as all_genres_csv:
		filewriter = csv.writer(all_genres_csv, delimiter=',')
		filewriter.writerow(['Artist'.encode('utf-8'), 'Title'.encode('utf-8'), 
			'Key'.encode('utf-8'), 'BPM'.encode('utf-8'), 'Genre'.encode('utf-8')])

		for url in url_list:
			track_url = url
			try:

				track_respone = urllib2.urlopen(track_url)

				track_html = track_respone.read()

				track_soup = soup(track_html, features="html.parser")

				key = track_soup.find("li", {'class':"interior-track-content-item interior-track-key"}).span.findNext('span').text

				# print(key)

				bpm = track_soup.find("li", {'class':'interior-track-content-item interior-track-bpm'}).span.findNext('span').text

				# print(bpm)


				genre = track_soup.find("li", {'class':"interior-track-content-item interior-track-genre"}).span.findNext('span').a.text
				
				# print(genre)

				artist = track_soup.find("div", {"class":"interior-track-artists"}).span.findNext('span').a.text

				song_title = track_soup.find("div", {"class":'interior-title'}).h1.text


				print(artist + ": " + song_title +", " + key + ", " + bpm + " bpm" + " Genre: " + genre)

				# with open('all_genres.csv', 'a') as all_genres_csv:
				# 	filewriter = csv.writer(all_genres_csv, delimiter=',')
				filewriter.writerow([artist.encode("utf-8"), song_title.encode("utf-8")
				, key.encode("utf-8"), bpm.encode("utf-8"), genre.encode("utf-8")])

			except:
				filewriter.writerow(['scrape failed'.encode("utf-8")])