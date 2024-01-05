from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunYorumModeli(TemelVeriSinifi):
    """
    Ürün Yorum Modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "yorum"
    :type __tablename__: str

    :cvar siparis_id: Yorumun bağlı olduğu sipariş ID'si
    :type siparis_id: Mapped[int]

    :cvar urun_id: Yorumun bağlı olduğu ürün ID'si
    :type urun_id: Mapped[int]

    :cvar yorum: Yorum metni
    :type yorum: Mapped[str]

    :cvar puan: Yorumun puanı
    :type puan: Mapped[float]
    """
    __tablename__ = "yorum"

    siparis_id:Mapped[int] = mapped_column(ForeignKey('siparis.id'))
    urun_id:Mapped[int] = mapped_column(ForeignKey('urun.id'))
    yorum:Mapped[str] =  mapped_column(nullable=True)
    puan:Mapped[float] = mapped_column(nullable=True)

