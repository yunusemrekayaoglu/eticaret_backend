from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunAlisModeli(TemelVeriSinifi):
    __tablename__ = "alis_hareketleri"

    urun_id:Mapped[int] = mapped_column(ForeignKey('urun.id'))
    miktar:Mapped[float] = mapped_column(nullable=False)
    birim_fiyat:Mapped[float] = mapped_column(nullable=False)
    tarih:Mapped[date] = mapped_column(default=date.today())