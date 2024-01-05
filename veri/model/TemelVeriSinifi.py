from datetime import datetime

from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class TemelVeriSinifi(DeclarativeBase):
    """
    Temel Veri Sınıfı.

    :cvar id: Veri nesnesinin benzersiz kimliği (primary key)
    :type id: Mapped[int]

    :cvar eklenme_tarihi: Veri nesnesinin eklenme tarihi
    :type eklenme_tarihi: Mapped[datetime]

    :cvar guncelleme_tarihi: Veri nesnesinin son güncellenme tarihi
    :type guncelleme_tarihi: Mapped[datetime]
    """

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    eklenme_tarihi: Mapped[datetime] = mapped_column(default=datetime.now())
    guncelleme_tarihi: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())

    def to_dict(self) -> dict:
        """
               Veriyi bir sözlük haline getirir.

               :return: Veriyi temsil eden sözlük
               :rtype: dict
               """
        sonuc = {col.key: getattr(self, col.key) for col in inspect(self).mapper.column_attrs}
        return sonuc
