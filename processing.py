from csv2json import *
import pandas as pd
import geopy.distance
# raw_df['time_int'] = int(raw_df['time'])
# by_time=raw_df.groupby("time_int")

distance=0.0
for i in range(len(raw_df)):
    if i != len(raw_df)-1:
        top_row = raw_df.iloc[i]
        bot_row = raw_df.iloc[i+1]
        top_point = (top_row['Latitude'],top_row['Longitude'])
        bot_point = (bot_row['Latitude'],bot_row['Longitude'])
        #print(top_point,bot_point)
        distance_point=(geopy.distance.geodesic(top_point,bot_point))
        distance = distance + float(str(distance_point)[:-3])
        print(distance)
print("Total Distance ", distance)