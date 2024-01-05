from sqlalchemy.orm import mapped_column, Mapped, relationship

from veri.model.TemelVeriSinifi import TemelVeriSinifi

#urun modelini yedim
#urun modelinin icinde kodu, adi, fiyati, ....,
class UrunModeli(TemelVeriSinifi):
    """
    Ürün Modeli.

    :cvar __tablename__: Veritabanındaki tablo adı: "urun"
    :type __tablename__: str

    :cvar urun_kodu: Ürün kodu
    :type urun_kodu: Mapped[str]

    :cvar adi: Ürün adı
    :type adi: Mapped[str]

    :cvar fiyati: Ürün fiyatı
    :type fiyati: Mapped[float]

    :cvar aciklama: Ürün açıklaması
    :type aciklama: Mapped[str]

    :cvar fotograf: Ürün fotoğrafı
    :type fotograf: Mapped[str]

    :cvar alislar: Ürünle ilgili alış hareketleri
    :type alislar: Mapped[list['UrunAlisModeli']]

    :cvar satislar: Ürünle ilgili satış hareketleri
    :type satislar: Mapped[list['UrunSatisModeli']]

    :property stok_miktari: Ürünün stok miktarı (alımlardan satışlar çıkartılarak hesaplanır)
    :rtype stok_miktari: float
    """
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
        """
               Ürünün stok miktarını hesaplar.

               :return: Ürünün stok miktarı
               :rtype: float
               """
        return sum([alis.miktar for alis in self.alislar]) - sum([satis.miktar for satis in self.satislar])
