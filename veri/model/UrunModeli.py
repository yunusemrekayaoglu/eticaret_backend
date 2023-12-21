from sqlalchemy.orm import mapped_column, Mapped, relationship

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunModeli(TemelVeriSinifi):
    __tablename__ = "urun"

    urun_kodu:Mapped[str] = mapped_column(nullable=False, unique=True)
    adi:Mapped[str] = mapped_column(nullable=False)
    fiyati:Mapped[float] = mapped_column(nullable=False)
    aciklama:Mapped[str] = mapped_column(nullable=False)
    fotograf:Mapped[str] = mapped_column(nullable=True) # STR aldım dbye kaydederken daha rahat olabilir
    alislar:Mapped[list['UrunAlisModeli']] = relationship()
    satislar:Mapped[list['UrunSatisModeli']] = relationship()

    @property
    def stok_miktari(self):
        return sum([alis.miktar for alis in self.alislar]) - sum([satis.miktar for satis in self.satislar])
