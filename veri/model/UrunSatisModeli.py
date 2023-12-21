from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunSatisModeli(TemelVeriSinifi):
    __tablename__ = "satis_modeli"

    urun_id: Mapped[int] = mapped_column(ForeignKey('urun.id'))
    miktar: Mapped[float] = mapped_column(nullable=False)
    birim_fiyat: Mapped[float] = mapped_column(nullable=False)
    tarih: Mapped[date] = mapped_column(default=date.today())