from sqlalchemy.orm import Mapped, mapped_column

from veri.model.TemelVeriSinifi import TemelVeriSinifi


class UrunKategoriModeli(TemelVeriSinifi):
    __tablename__ = "kategori"

    kategori:Mapped[str] = mapped_column(nullable=False)
    