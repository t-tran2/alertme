from flask import Flask
from get_road_name import get_road_name
from search_crashes import search_crashes

app = Flask(__name__)
@app.route('/alertme/', methods=['GET', 'POST'])
def get_warning(points):
    road_names = get_road_name(points[1])
    warning = search_crashes(road_names)
    return warning
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)