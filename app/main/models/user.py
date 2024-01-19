from uuid import uuid4
from datetime import datetime
from .. import db, bcrypt
from .base import BaseModel


class RoleAndCCTVListUDT(db.UserType):
    role = db.columns.Text()
    cctv_list = db.columns.Set(db.columns.Text())


class User(BaseModel):
    """
        User Model for storing user related details
    """

    name = db.columns.Text()
    phone = db.columns.Text()
    email = db.columns.Text()
    username = db.columns.Text()
    password = db.columns.Text()
    org_ids = db.columns.Set(db.columns.UUID())
    extra = db.columns.Map(
        key_type=db.columns.Text(),
        value_type=db.columns.Text()
    )
    # parent_id_role_cctv_data = db.columns.Map(
    #     key_type=db.columns.Text(),
    #     value_type=db.columns.UserDefinedType(RoleAndCCTVListUDT)
    # )

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
