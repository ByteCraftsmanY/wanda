from flask import request
from flask_restx import Resource
from http import HTTPStatus

from ..dtos.cctv_dto import api, CCTVDto, CreateCCTVDto, UpdateCCTVDto
from ..services.cctv_service import CCTVService

api = api
_cctv = CCTVDto.cctv
create_cctv = CreateCCTVDto.cctv
update_cctv = UpdateCCTVDto.cctv
cctv_service = CCTVService()


@api.route('/<cctv_id>')
@api.param('cctv_id', 'CCTV id')
@api.response(HTTPStatus.NOT_FOUND, 'cctv not found')
class CCTV(Resource):
    @api.doc('get cctv information')
    @api.marshal_with(_cctv)
    def get(self, cctv_id):
        return cctv_service.get_by_id(cctv_id)

    @api.doc('get cctv information')
    @api.response(HTTPStatus.NO_CONTENT, description='cctv info deleted')
    def delete(self, cctv_id):
        return cctv_service.delete_by_id(cctv_id)


@api.route('/')
class CCTVList(Resource):

    @api.doc('List of registered users')
    @api.marshal_list_with(_cctv, envelope='data')
    def get(self):
        return cctv_service.get_all()

    @api.doc('create new cctv')
    @api.expect(create_cctv, validate=True)
    @api.marshal_with(_cctv)
    @api.response(HTTPStatus.CREATED, 'cctv registered successfully')
    def post(self):
        data = request.json
        result = cctv_service.create(data)
        if result:
            return result
        api.abort(HTTPStatus.NOT_FOUND, message=f"Record with id {data.get('id')} not found")

    @api.doc('update cctv')
    @api.expect(update_cctv, validate=True)
    @api.marshal_with(_cctv)
    def patch(self):
        data = request.json
        result = cctv_service.update(data)
        if result:
            return result
        api.abort(HTTPStatus.NOT_FOUND, message=f"Record with id {data.get('id')} not found")
