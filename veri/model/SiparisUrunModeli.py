from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class SiparisUrunModeli(TemelVeriSinifi):
    """
    Sipariş Ürün modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "siparis_urun"
    :type __tablename__: str

    :cvar siparis_id: Ürünün bağlı olduğu sipariş ID'si
    :type siparis_id: Mapped[int]
    :cvar urun_id: Ürün ID'si
    :type urun_id: Mapped[int]
    :cvar adet: Ürün adedi
    :type adet: Mapped[float]
    :cvar birim_fiyat: Ürün birim fiyatı
    :type birim_fiyat: Mapped[float]
    """

    __tablename__ = "siparis_urun"

    siparis_id:Mapped[int] = mapped_column(ForeignKey('siparis.id'))
    urun_id:Mapped[int] = mapped_column(ForeignKey('urun.id'))
    adet:Mapped[float] = mapped_column(nullable=False)
    birim_fiyat:Mapped[float] = mapped_column(nullable=False)

