from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class SiparisModeli(TemelVeriSinifi):
    """
        Sipariş modeli.

        :cvar __tablename__: Veritabanındaki tablo adı: "siparis"
        :type __tablename__: str

        :cvar tarih: Sipariş tarihi
        :type tarih: Mapped[datetime]
        :cvar magaza_id: Siparişin bağlı olduğu mağaza ID'si
        :type magaza_id: Mapped[int]
        :cvar musteri_id: Siparişin bağlı olduğu müşteri ID'si
        :type musteri_id: Mapped[int]
        """


    __tablename__ = "siparis"

    tarih:Mapped[datetime] = mapped_column(default=datetime.now())
    magaza_id:Mapped[int] = mapped_column(ForeignKey('magaza.id'))
    musteri_id:Mapped[int] = mapped_column(ForeignKey('musteri.id'))

