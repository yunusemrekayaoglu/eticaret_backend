from flask import Blueprint

from blueprints.genelBP import genel_bp
from veri import MagazaModeli, MusteriModeli, SiparisModeli, SiparisUrunModeli, UrunAlisModeli, UrunSatisModeli, \
    UrunKategoriModeli, UrunModeli, UrunOzellikleriModeli, UrunYorumModeli


"""

Buraya blueprintleri ekliyoruz.
Blueprintlerin url prefixlerini belirliyoruz.
Blueprintlerin içine veri tabanı modelini ve blueprint adını gönderiyoruz.
Blueprintlerin içindeki fonksiyonlar veri tabanı modeli ile ilgili kayıtları getirir, ekler, düzenler ve siler.
"""


v1_bp = Blueprint("v1_bp", __name__)
v1_bp.register_blueprint(genel_bp(MagazaModeli, 'magaza_bp'), url_prefix="/magaza")
v1_bp.register_blueprint(genel_bp(MusteriModeli, 'musteri_bp'), url_prefix="/musteri")
v1_bp.register_blueprint(genel_bp(SiparisModeli, 'siparis_bp'), url_prefix="/siparis")
v1_bp.register_blueprint(genel_bp(SiparisUrunModeli, 'siparis_urun_bp'), url_prefix="/siparis_urun")
v1_bp.register_blueprint(genel_bp(UrunAlisModeli, 'urun_alis_bp'), url_prefix="/urun_alis")
v1_bp.register_blueprint(genel_bp(UrunKategoriModeli, 'urun_kategori_bp'), url_prefix="/urun_kategori")
v1_bp.register_blueprint(genel_bp(UrunModeli, 'urun_bp'), url_prefix="/urun")
v1_bp.register_blueprint(genel_bp(UrunOzellikleriModeli, 'urun_ozellikleri_bp'), url_prefix="/urun_ozellikleri")
v1_bp.register_blueprint(genel_bp(UrunSatisModeli, 'urun_satis_bp'), url_prefix="/urun_satis")
v1_bp.register_blueprint(genel_bp(UrunYorumModeli, 'urun_yorum_bp'), url_prefix="/urun_yorum")




api_bp = Blueprint("api_bp", __name__)
api_bp.register_blueprint(v1_bp, url_prefix="/v1")