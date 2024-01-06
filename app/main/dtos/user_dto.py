from flask_restx import Namespace, fields

api = Namespace('user')

parent_id_role_cctv_data = api.model('ParentIdAndRoleAndCCTVData', {
    'role': fields.String(description='user role corresponding to pid'),
    'cctv_list': fields.List(fields.String, description='cctv list corresponding to pid'),
})


class UserDto:
    user = api.model('user', {
        'name': fields.String(required=True, description='user name'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'parent_id_role_cctv_data': fields.Nested(
            parent_id_role_cctv_data,
            description='User Role and List of CCTV Ids corresponding to ParentID'
        ),
    })


class CreateUserDto(UserDto):
    user = api.model('user', {
        'name': fields.String(required=True, description='user name'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'parent_id_role_cctv_data': fields.Nested(
            parent_id_role_cctv_data,
            description='User Role and List of CCTV Ids corresponding to ParentID'
        )
    })


class UpdateUserDto(CreateUserDto):
    user = api.model('user', {
        'name': fields.String(required=True, description='user name'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'parent_id_role_cctv_data': fields.Nested(
            parent_id_role_cctv_data,
            description='User Role and List of CCTV Ids corresponding to ParentID'
        )
    })
