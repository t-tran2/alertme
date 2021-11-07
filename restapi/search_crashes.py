import pandas as pd
from calc_distance import calc_distance

# Test: delete these later
# Load crashclean2.csv dataset into dataframe
test_df = pd.read_csv("data/crashclean2.csv", low_memory=False)
# Dataframe with only columns of interest
columns = ['LocalReportNumber', 'Latitude', 'Longitude', 'LocationRoadName']
test_df = test_df[columns]

def search_crashes(road_names, crash_df, lat, long):
    # Concatanate road_names into format for parameter in str.contains
    road_names_str = "|".join(road_names)
    # Filter rows based on substring of road names
    filtered_crash_df = crash_df[crash_df["LocationRoadName"].str.contains(road_names_str, case=False, na=False)]
    
    # Choose crash with x mile radius of current location
    for index, row in filtered_crash_df.iterrows():
        crash_lat = row['Latitude']
        crash_long = row['Longitude']
        distance = calc_distance(lat, long, crash_lat, crash_long)
        # max distance (miles) from crash to warn driver
        distance_threshold = 2
        warning_msg = "Crash prone zone, please be cautious"
        if distance < distance_threshold:
            return warning_msg

    # Delete later
    # test_df = filtered_crash_df[filtered_crash_df["LocationRoadName"] == "Shrock"]
    # print(test_df.head(10))


# test
print(search_crashes(["shrock", "broad"], test_df, 39.98525,	-82.79114))