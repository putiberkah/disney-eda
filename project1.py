#SCRUTINIZE THE DATA

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#LOADING THE DATASET

disney = pd.read_csv('disney_plus_titles.csv', sep = ",")
#print(disney.head())
#print("Shape is: ", disney.shape)
#print(disney.info())

#DATA CLEANING

#Check if there is any missing data
#print(disney.isnull().sum())

#show rows containing missing value in rating
#print(disney[disney['rating'].isnull()])

#UPDATE RATING WHICH IS NULL

disney.loc[4, ["rating"]] = ["PG-13"]
disney.loc[276, ["rating"]] = ["PG-13"]
disney.loc[280, ["rating"]] = ["TV-14"]

#UPDATE NULL TO UNKNOWN

disney["cast"] = disney["cast"].fillna("unknown")
disney["director"] = disney["director"].fillna("unknown")
disney["country"] = disney["country"].fillna("unknown")
disney["date_added"] = disney["date_added"].fillna("unknown")
#print(disney.isnull().sum())

#print(disney["country"].unique())
#PREPARING ON MAKING HISTOGRAM OF RELEASE YEAR

#print("Release year is from ", disney['release_year'].min()," to ", disney['release_year'].max())

#plt.hist(disney['release_year'], bins=10)
#plt.title('Release Year')
#plt.savefig('release_year.png')

#DELETE ROWS WHICH CONTAIN NULL VALUE

#disney = disney.dropna(how = 'any', axis = 0)

#RE-CHECK 

#print("Shape is: ", disney.shape)
#print(disney.isnull().sum())

#CHECK DUPLICATE

#duplicated = disney.duplicated()
#print(duplicated.sum())

#STATISTICAL INSIGHT

#print(disney.value_counts(["rating"]))
#print(disney['type'].value_counts())
#print(disney['duration'].describe())

#DATA VISUALIZATION

#sns.set_style('darkgrid')
#sns.countplot(y='type',data=disney,palette='colorblind')
#plt.xlabel('Count')
#plt.ylabel('Type')
#plt.title('Movie Type in Disney+')
#plt.savefig('Type_new.png')

#sns.countplot(y='rating',data=disney,palette='colorblind')
#plt.xlabel('Count')
#plt.ylabel('Rating')
#plt.title('Movie Rating in Disney+')
#plt.savefig('rating.png')

fig = plt.figure(figsize=(10,6))
n, bins, patches = plt.hist(disney['release_year'])

plt.xticks(bins)
plt.grid(axis='x', lw = 0.5)

plt.title('Release Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.savefig('011 - 2.png')