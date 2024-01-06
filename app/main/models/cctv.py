from uuid import uuid4
from datetime import datetime

from .. import db


class CCTV(db.Model):
    """
        CCTV Model for storing cctv camera related details
    """

    id = db.columns.UUID(partition_key=True, primary_key=True, default=uuid4)
    name = db.columns.Text()
    rtsp_url = db.columns.Text()
    is_active = db.columns.Boolean(default=True)
    created_at = db.columns.DateTime(default=datetime.now())
    updated_at = db.columns.DateTime(default=datetime.now())
