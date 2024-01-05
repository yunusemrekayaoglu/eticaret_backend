from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunOzellikleriModeli(TemelVeriSinifi):
    """
    Ürün Özellikleri Modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "urun_ozellik"
    :type __tablename__: str

    :cvar urun_id: Ürün özelliğinin bağlı olduğu ürün ID'si
    :type urun_id: Mapped[int]

    :cvar ozellik: Ürün özelliği
    :type ozellik: Mapped[str]

    :cvar deger: Ürün özelliği değeri (alış ile satış arasındaki kâr)
    :type deger: Mapped[float]
    """
    __tablename__ = "urun_ozellik"

    urun_id: Mapped[int] = mapped_column(ForeignKey('magaza.id'))
    ozellik:Mapped[str] = mapped_column(nullable=False)
    deger:Mapped[float] = mapped_column(nullable=False) #alış ile satış arasındaki kâr

    
