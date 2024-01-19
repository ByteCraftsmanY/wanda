from flask_restx import Namespace, fields

api = Namespace('cctv')


class CCTVDto:
    cctv = api.model('cctv', {
        'uuid': fields.String(description='cctv id'),
        'username': fields.String(required=True, description='cctv name'),
        'is_active': fields.Boolean(),
        'url': fields.String(required=True, description='cctv rtsp url [streaming url]'),
        'created_at': fields.DateTime(),
        'updated_at': fields.DateTime(),
        'deleted_at': fields.DateTime(),
    })


class CreateCCTVDto(CCTVDto):
    cctv = api.model('cctv', {
        'username': fields.String(required=True, description='cctv username'),
        'password': fields.String(required=True, description='cctv password'),
        'is_active': fields.Boolean(),
        'url': fields.String(required=True, description='cctv url [streaming/rtsp url]'),
    })


class UpdateCCTVDto(CCTVDto):
    cctv = api.model('cctv', {
        'id': fields.String(required=True, description='cctv id'),
        'username': fields.String(description='cctv name'),
        'is_active': fields.Boolean(),
        'url': fields.String(description='cctv url [streaming/rtsp url]'),
    })
