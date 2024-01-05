from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunKategoriModeli(TemelVeriSinifi):
    """
    Ürün Kategori Modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "kategori"
    :type __tablename__: str

    :cvar kategori: Ürün kategorisi
    :type kategori: Mapped[str]
    """
    __tablename__ = "kategori"

    kategori:Mapped[str] = mapped_column(nullable=False)
    