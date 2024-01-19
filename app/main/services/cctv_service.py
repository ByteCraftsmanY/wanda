from uuid import uuid4
from datetime import datetime
from ..models.cctv import CCTV


class CCTVService:
    def create(self, data):
        return CCTV.create(
            **data,
        )

    def get_all(self):
        return CCTV.all()

    def get_by_id(self, _id):
        cctv = CCTV.get(uuid=_id)
        if not cctv:
            return
        return cctv

    def update(self, data):
        cctv = self.get_by_id(_id=data.get('id'))
        if not cctv:
            return
        data['updated_at'] = datetime.now()
        return CCTV(**data).update()

    def delete_by_id(self, _id):
        return CCTV(uuid=_id).delete()
