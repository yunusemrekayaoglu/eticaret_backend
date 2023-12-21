from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class MagazaModeli(TemelVeriSinifi):
    __tablename__ = "magaza"

    adi: Mapped[str] = mapped_column(nullable=False)
    adres: Mapped[str] = mapped_column(nullable=False)
    telefon: Mapped[str] = mapped_column(nullable=False)
    yetkili: Mapped[str] = mapped_column(nullable=False)
