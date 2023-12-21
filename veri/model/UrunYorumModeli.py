from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunYorumModeli(TemelVeriSinifi):
    __tablename__ = "yorum"

    siparis_id:Mapped[int] = mapped_column(ForeignKey('siparis.id'))
    urun_id:Mapped[int] = mapped_column(ForeignKey('urun.id'))
    yorum:Mapped[str] =  mapped_column(nullable=True)
    puan:Mapped[float] = mapped_column(nullable=True)

