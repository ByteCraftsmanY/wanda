from flask_restx import Api
from flask import Blueprint

from .main.controllers.health_controller import api as health_ns
from .main.controllers.cctv_controller import api as cctv_ns
from .main.controllers.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api_v1 = Api(
    blueprint,
    title="Vision",
    version='1.0',
    description='flask api',
    doc='/',
    prefix='/api/v1'
)

api_v1.add_namespace(health_ns)
api_v1.add_namespace(cctv_ns)
api_v1.add_namespace(user_ns)
