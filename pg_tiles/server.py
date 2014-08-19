from flask import Flask, Blueprint, render_template

tileserver = Blueprint('tiles', __name__)
web_ui = Blueprint('web_ui', __name__, template_folder='templates')


@tileserver.route('/{layer}/{z}/{x}/{y}')
def serve_tile(layer, z, x, y):
    # todo: find the layer from configuration, determine the bounding
    # box, return geojson containing all features in the bounding box
    pass


@web_ui.route('/')
def leaflet_map():
    return render_template('leaflet.html')


def main():
    app = Flask(__name__)
    app.register_blueprint(tileserver, url_prefix='/tiles')
    app.register_blueprint(web_ui, url_prefix='')
    app.run(debug=True)

if __name__ == '__main__':
    main()
