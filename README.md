# beatport-scraper
This project includes a web scraper that pulls text information from the Beatport top 100 for a variety of genres and creates a csv file based on this info
It includes a program with simple functions to analyze this info by genre and produces bar charts accordingly
It is seperated into 3 scripts: the first grabs the urls for all songs, and writes them to a text file. The second uses these urls to access each songs deidicated web page, which has detailed info such as key and bpm, and writes this info to a csv file. the third script analyzes this csv file to produce histograms that display song distribution by key and bpm for each genre.
