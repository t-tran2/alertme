from flask import Flask

from alertme.restapi.get_road_name import get_road_name
app = Flask(__name__)
@app.route('/alertme/', methods=['GET', 'POST'])
def get_warning(points):
    get_road_name(points[1])
    return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)