from .BaseModel import BaseModel


class Waybill(BaseModel):

    class Status:
        OPEN = 'open'
        PROCESSED = 'processed'

    _collection = 'waybill'
