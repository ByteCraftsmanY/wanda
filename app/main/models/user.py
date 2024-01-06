from uuid import uuid4
from datetime import datetime
from .. import db, bcrypt


class RoleAndCCTVListUDT(db.UserType):
    role = db.columns.Text()
    cctv_list = db.columns.Set(db.columns.Text())


class User(db.Model):
    """
        User Model for storing user related details
    """

    id = db.columns.UUID(partition_key=True, primary_key=True, default=uuid4)
    name = db.columns.Text()
    email = db.columns.Text()
    username = db.columns.Text()
    parent_id_role_cctv_data = db.columns.Map(
        key_type=db.columns.Text(),
        value_type=db.columns.UserDefinedType(RoleAndCCTVListUDT)
    )
    password_hash = db.columns.Text()
    created_at = db.columns.DateTime(default=datetime.now())
    updated_at = db.columns.DateTime(default=datetime.now())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.name}>"
