from http import HTTPStatus
from flask import request
from flask_restx import Resource

from ..dtos.user_dto import *
from ..services.user_service import UserService

_user = UserDto.user
create_user = CreateUserDto.user
userService = UserService()


@api.route('/')
class UserList(Resource):
    @api.doc('List of registered users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return userService.get_all()

    @api.response(HTTPStatus.CREATED, 'User successfully created')
    @api.doc("create a new user")
    @api.expect(create_user, validate=True)
    @api.marshal_with(_user)
    def post(self):
        data = request.json
        return userService.save(data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(HTTPStatus.NOT_FOUND, 'User not found')
class User(Resource):
    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, public_id):
        user = userService.get_by_id(public_id)
        if user:
            return user
        api.abort(HTTPStatus.NOT_FOUND)
