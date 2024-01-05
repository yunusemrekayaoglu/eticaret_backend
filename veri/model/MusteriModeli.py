from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class MusteriModeli(TemelVeriSinifi):

    """
    Müşteri modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "musteri"
    :type __tablename__: str

    :cvar ad: Müşteri adı
    :type ad: Mapped[str]
    :cvar soyad: Müşteri soyadı
    :type soyad: Mapped[str]
    :cvar telefon: Müşteri telefon numarası
    :type telefon: Mapped[str]
    :cvar adres: Müşteri adresi
    :type adres: Mapped[str]
    :cvar fotograf: Müşteri fotoğrafı
    :type fotograf: Mapped[str]
    """


    __tablename__ = "musteri"

    ad:Mapped[str] = mapped_column(nullable=False)
    soyad:Mapped[str] = mapped_column(nullable=False)
    telefon:Mapped[str] = mapped_column(nullable=False)
    adres:Mapped[str] = mapped_column(nullable=False)
    fotograf:Mapped[str] = mapped_column(nullable=True)