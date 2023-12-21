from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class SiparisModeli(TemelVeriSinifi):
    __tablename__ = "siparis"

    tarih:Mapped[datetime] = mapped_column(default=datetime.now())
    magaza_id:Mapped[int] = mapped_column(ForeignKey('magaza.id'))
    musteri_id:Mapped[int] = mapped_column(ForeignKey('musteri.id'))

