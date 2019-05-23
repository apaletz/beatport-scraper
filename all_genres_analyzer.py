import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

#create initial dataframe from csv file
tracks = pd.read_csv("all_genres_1.csv")

#create genres dataframe
genres = tracks.Genre.unique()

#a function to create bar charts that show a given creteria by genere
def chart_maker(criteria):
	for genre in genres:
		genre_df = tracks.loc[tracks['Genre'] == genre]
		print(genre)

		print(genre_df[criteria].value_counts())
		criteriaArray = genre_df[criteria].value_counts()

		bar = criteriaArray.plot.bar(title=genre + 'tracks by ' + criteria)
		plt.show()

#a function to create bar charts that show a given criteria for all tracks
def all_by_criteria(criteria):
	all_tracks = tracks[criteria].value_counts()
	graph = all_tracks.plot.bar(title = "All tracks by " + criteria)
	plt.show()

chart_maker('Key')
all_by_criteria('Key')

chart_maker('BPM')
all_by_criteria('BPM')