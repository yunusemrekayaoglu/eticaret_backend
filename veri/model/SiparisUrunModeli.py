from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class SiparisUrunModeli(TemelVeriSinifi):
    __tablename__ = "siparis_urun"

    siparis_id:Mapped[int] = mapped_column(ForeignKey('siparis.id'))
    urun_id:Mapped[int] = mapped_column(ForeignKey('urun.id'))
    adet:Mapped[float] = mapped_column(nullable=False)
    birim_fiyat:Mapped[float] = mapped_column(nullable=False)

