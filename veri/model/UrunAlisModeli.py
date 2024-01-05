from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunAlisModeli(TemelVeriSinifi):
    """
    Ürün Alış Modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "alis_hareketleri"
    :type __tablename__: str

    :cvar urun_id: Alış hareketinin bağlı olduğu ürün ID'si
    :type urun_id: Mapped[int]

    :cvar miktar: Alınan ürün miktarı
    :type miktar: Mapped[float]

    :cvar birim_fiyat: Birim fiyat
    :type birim_fiyat: Mapped[float]

    :cvar tarih: Alış tarihi
    :type tarih: Mapped[date]
    """


    __tablename__ = "alis_hareketleri"

    urun_id:Mapped[int] = mapped_column(ForeignKey('urun.id'))
    miktar:Mapped[float] = mapped_column(nullable=False)
    birim_fiyat:Mapped[float] = mapped_column(nullable=False)
    tarih:Mapped[date] = mapped_column(default=date.today())