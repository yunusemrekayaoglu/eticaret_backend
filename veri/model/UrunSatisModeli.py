from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunSatisModeli(TemelVeriSinifi):
    """
    Ürün Satış Modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "satis_modeli"
    :type __tablename__: str

    :cvar urun_id: Satışın bağlı olduğu ürün ID'si
    :type urun_id: Mapped[int]

    :cvar miktar: Satılan ürün miktarı
    :type miktar: Mapped[float]

    :cvar birim_fiyat: Birim fiyat
    :type birim_fiyat: Mapped[float]

    :cvar tarih: Satış tarihi
    :type tarih: Mapped[date]
    """

    __tablename__ = "satis_modeli"

    urun_id: Mapped[int] = mapped_column(ForeignKey('urun.id'))
    miktar: Mapped[float] = mapped_column(nullable=False)
    birim_fiyat: Mapped[float] = mapped_column(nullable=False)
    tarih: Mapped[date] = mapped_column(default=date.today())