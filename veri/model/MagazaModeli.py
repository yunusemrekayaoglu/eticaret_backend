from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class MagazaModeli(TemelVeriSinifi):
    """
    Mağaza modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "magaza"
    :type __tablename__: str

    :cvar adi: Mağaza adı
    :type adi: Mapped[str]
    :cvar adres: Mağaza adresi
    :type adres: Mapped[str]
    :cvar telefon: Mağaza telefon numarası
    :type telefon: Mapped[str]
    :cvar yetkili: Mağaza yetkilisi
    :type yetkili: Mapped[str]
    """

    __tablename__ = "magaza"

    adi: Mapped[str] = mapped_column(nullable=False)
    adres: Mapped[str] = mapped_column(nullable=False)
    telefon: Mapped[str] = mapped_column(nullable=False)
    yetkili: Mapped[str] = mapped_column(nullable=False)
