from uuid import uuid4
from datetime import datetime
from werkzeug.exceptions import NotFound
from .. import db


class BaseModel(db.Model):
    """
        Base Model for all models
    """
    __abstract__ = True
    uuid = db.columns.UUID(primary_key=True,partition_key=True, default=uuid4)
    is_active = db.columns.Boolean(default=True)
    created_at = db.columns.DateTime(default=datetime.utcnow())
    updated_at = db.columns.DateTime(default=datetime.utcnow())
    deleted_at = db.columns.DateTime(default=None)

    def __repr__(self):
        return "<{}:{}>".format(self.__class__.__name__, self.id)

