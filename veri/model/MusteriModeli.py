from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class MusteriModeli(TemelVeriSinifi):
    __tablename__ = "musteri"

    ad:Mapped[str] = mapped_column(nullable=False)
    soyad:Mapped[str] = mapped_column(nullable=False)
    telefon:Mapped[str] = mapped_column(nullable=False)
    adres:Mapped[str] = mapped_column(nullable=False)
    fotograf:Mapped[str] = mapped_column(nullable=True)