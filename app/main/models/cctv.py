from .. import db
from .base import BaseModel


class CCTV(BaseModel):
    """
        CCTV Model for storing cctv camera related details
    """
    username = db.columns.Text()
    password = db.columns.Text()
    url = db.columns.Text()
    organization_id = db.columns.UUID()
    extra = db.columns.Map(db.columns.Text(), db.columns.Text())

    def __repr__(self):
        return "<CCTV '{}'>".format(self.uuid)
