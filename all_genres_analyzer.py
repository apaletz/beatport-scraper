import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

tracks = pd.read_csv("all_genres_1.csv")

# print(tracks)

# print(tracks.Genre.unique())

genres = tracks.Genre.unique()

print(tracks.Artist)

for genre in genres:
	genre_df = tracks.loc[tracks['Genre'] == genre]
	print(genre)


	print(genre_df['Key'].value_counts())
	# keyArray = genre_df['Key'].value_counts()
	# print(str(keyArray.size())

	keyArray = genre_df['Key'].value_counts()

	bar = keyArray.plot.bar(title=genre + " tracks by key")

	plt.show()


all_tracks_keys = tracks['Key'].value_counts()

print(all_tracks_keys)

graph = all_tracks_keys.plot.bar(title="All tracks by key")

plt.show()