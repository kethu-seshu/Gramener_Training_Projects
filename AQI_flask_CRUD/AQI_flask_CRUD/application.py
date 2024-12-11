from flask import Flask, jsonify, redirect
from flask_restful import Api, MethodNotAllowed, NotFound
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from resources.swaggerConfig import SwaggerConfig
from util.common import domain, port, prefix, build_swagger_config_json
from resources.airQualityResource import (
    AirQualityGETResource,
    AirQualityEntryGETResource,
    AirQualityPOSTResource,
    AirQualityPUTResource,
    AirQualityDELETEResource
)

application = Flask(__name__)
app = application
app.config['PROPAGATE_EXCEPTIONS'] = True
CORS(app)
api = Api(app, prefix=prefix, catch_all_404s=True)

build_swagger_config_json()
swaggerui_blueprint = get_swaggerui_blueprint(
    prefix,
    f'http://{domain}:{port}{prefix}/swagger-config',
    config={
        'app_name': "Air Quality API",
        "layout": "BaseLayout",
        "docExpansion": "none"
    },
)
app.register_blueprint(swaggerui_blueprint)

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = jsonify({"message": str(e)})
    response.status_code = 404
    return response

@app.errorhandler(MethodNotAllowed)
def handle_method_not_allowed(e):
    response = jsonify({"message": str(e)})
    response.status_code = 405
    return response

@app.route('/')
def redirect_to_prefix():
    if prefix != '':
        return redirect(prefix)

# Add Resources
api.add_resource(SwaggerConfig, '/swagger-config')
api.add_resource(AirQualityGETResource, '/air-quality')
api.add_resource(AirQualityEntryGETResource, '/air-quality/<int:id>')
api.add_resource(AirQualityPOSTResource, '/air-quality')
api.add_resource(AirQualityPUTResource, '/air-quality/<int:id>')
api.add_resource(AirQualityDELETEResource, '/air-quality/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
