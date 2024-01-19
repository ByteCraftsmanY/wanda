from flask_restx import Resource

from ..dtos.health_dto import HealthDto
from http import HTTPStatus

api = HealthDto.api


@api.route('/')
class Health(Resource):
    @api.doc('check app health')
    @api.response(code=HTTPStatus.OK, description='app health')
    def get(self):
        return {
            'status': 'success',
            'app_status': 'healthy'
        }
