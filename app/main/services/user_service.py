from uuid import uuid4
from datetime import datetime

from ..models.user import User
from .. import bcrypt

class UserService:

    def save(self, data):
        data['password_hash'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        del data['password']

        return User.create(
            id=uuid4(),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            **data
        )

    def get_all(self):
        return User.all()

    def get_by_id(self, _id):
        user = User.get(id=_id)
        if not user:
            return
        return user

    def update(self, data):
        user = self.get_by_id(_id=data.get('id'))
        if not user:
            return
        data['updated_at'] = datetime.now()
        return User(**data).save()

    def delete_by_id(self, _id):
        return User(id=_id).delete()
