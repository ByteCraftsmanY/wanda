from flask_restx import Namespace, fields

api = Namespace('cctv')


class CCTVDto:
    cctv = api.model('cctv', {
        'id': fields.String(description='cctv id'),
        'name': fields.String(required=True, description='cctv name'),
        'is_active': fields.Boolean(),
        'rtsp_url': fields.String(required=True, description='cctv rtsp url [streaming url]'),
        'created_at': fields.DateTime(),
        'updated_at': fields.DateTime(),
    })


class CreateCCTVDto(CCTVDto):
    cctv = api.model('cctv', {
        'name': fields.String(required=True, description='cctv name'),
        'is_active': fields.Boolean(),
        'rtsp_url': fields.String(required=True, description='cctv rtsp url [streaming url]'),
    })


class UpdateCCTVDto(CCTVDto):
    cctv = api.model('cctv', {
        'id': fields.String(required=True, description='cctv id'),
        'name': fields.String(required=True, description='cctv name'),
        'is_active': fields.Boolean(),
        'rtsp_url': fields.String(required=True, description='cctv rtsp url [streaming url]'),
    })
