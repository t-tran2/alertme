from flask import Flask, request
from get_road_name import get_road_name
from search_crashes import search_crashes
import pandas as pd

# Load crashclean2.csv dataset into dataframe
crash_df = pd.read_csv("../data/crashclean2.csv", low_memory=False)
# Columns of interest
columns = ['LocalReportNumber', 'Latitude', 'Longitude', 'LocationRoadName']
crash_df = crash_df[columns]

app = Flask(__name__)

# Function to test server is running properly
@app.route('/', methods=['GET', 'POST'])
def test_endpoint():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return param1 + param2

# Example request: localhost:5000/?lat=31.24&long=-23.14
@app.route('/alertme/', methods=['GET', 'POST'])
def get_warning():
    # Get url parameters
    lat = request.args.get("lat")
    long = request.args.get("long")

    road_names = get_road_name(lat, long)
    warning = search_crashes(road_names, crash_df, lat, long)
    return warning
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)