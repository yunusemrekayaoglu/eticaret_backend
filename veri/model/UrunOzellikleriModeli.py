from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunOzellikleriModeli(TemelVeriSinifi):
    __tablename__ = "urun_ozellik"

    urun_id: Mapped[int] = mapped_column(ForeignKey('magaza.id'))
    ozellik:Mapped[str] = mapped_column(nullable=False)
    deger:Mapped[float] = mapped_column(nullable=False) #alış ile satış arasındaki kâr

    
