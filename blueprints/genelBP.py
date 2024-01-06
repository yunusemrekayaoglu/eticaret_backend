from flask import Blueprint, request, abort
from sqlalchemy import select, inspect, func

from blueprints.VeriSorgulama import sorgula
from veri import db


def genel_bp(veri_sinifi:type, bp_adi: str = 'genel_bp'):
    """
    Blueprint oluşturur. Blueprint adı verilmezse genel_bp olarak oluşturur.
    Blueprint ile veri tabanı modeli arasında ilişki kurar.

    :param veri_sinifi: Veri tabanı modeli
    :param bp_adi: Blueprint adı (varsayılan: 'genel_bp')
    :type bp_adi: str
    :return: Blueprint

    **İşlevler:**

    - :func:`index`: Veri tabanı modeli ile ilgili kayıtları sayfa ve kayıt sayısı parametrelerine göre getirir.
    - :func:`ekle`: Veri tabanı modeli ile ilgili kayıt ekler.
    - :func:`getir`: Veri tabanı modeli ile ilgili kayıt getirir.
    - :func:`duzenle`: Veri tabanı modeli ile ilgili kayıt düzenler.
    - :func:`sil`: Veri tabanı modeli ile ilgili kayıt siler.
    """

    bp = Blueprint(bp_adi, __name__)
    @bp.route('/', methods=['GET'])
    @bp.route('', methods=['GET'])
    @bp.route('/sayfa/<int:sayfa>', methods=['GET'])
    @bp.route('/sayfa/<int:sayfa>/<int:kayit_sayisi>', methods=['GET'])
    def index(sayfa: int = 1, kayit_sayisi: int = 10):

        """
        :param sayfa:
        :param kayit_sayisi:
        :return:

        Veri tabanı modeli ile ilgili kayıtları sayfa ve kayıt sayısı parametrelerine göre getirir.


        """

        sorgu = select(veri_sinifi)

        sayfa = max(0, sayfa
                    )

        sorgu = sorgula(sorgu, veri_sinifi, sayfa - 1, kayit_sayisi)


        cevap = db.session.scalars(sorgu).all()

        return [veri_sinifi.to_dict() for veri_sinifi in cevap]

    @bp.route('/sayfa_sayisi', methods=['GET'])
    @bp.route('/sayfa_sayisi/<int:kayit_sayisi>', methods=['GET'])
    def sayfa_sayisi(kayit_sayisi:int = 10):
        sorgu = select(func.count('*')).select_from(veri_sinifi)
        sorgu = sorgula(sorgu, veri_sinifi, - 1, kayit_sayisi)
        cevap = db.session.scalars(sorgu).all()
        kalan = cevap[0] % kayit_sayisi
        sayfa_sayisi = cevap[0] // kayit_sayisi
        if kalan > 0:
            sayfa_sayisi += 1
        return {'sayfa_sayisi': sayfa_sayisi}

    @bp.route('/', methods=['POST'])
    @bp.route('', methods=['POST'])
    def ekle():

        """
        :return:

        Veri tabanı modeli ile ilgili kayıt ekler.
        """
        veri = veri_sinifi()

        sutunlar = [col.key for col in inspect(veri).mapper.column_attrs]


        for sutun in request.json:
            if sutun in sutunlar:
                setattr(veri, sutun, request.json[sutun])
            else:
                return abort(500)

        db.session.add(veri)
        db.session.commit()

        return veri.to_dict()

    @bp.route('/<int:id>', methods=['GET'])
    def getir(id: int):

        """

        :param id:
        :return:


        Veri tabanı modeli ile ilgili kayıt getirir.
        """
        sorgu = select(veri_sinifi).where(veri_sinifi.id == id)

        cevap = db.session.scalars(sorgu).one()

        return cevap.to_dict()

    @bp.route("/<int:id>", methods=["PUT", "PATCH"])
    def duzenle(id: int):

        """

        :param id:
        :return:

        Veri tabanı modeli ile ilgili kayıt düzenler.
        """
        sorgu = select(veri_sinifi).where(veri_sinifi.id == id)
        veri = db.session.scalars(sorgu).one()

        sutunlar = [col.key for col in inspect(veri_sinifi).mapper.column_attrs]

        for sutun in request.json:
            if sutun in sutunlar:
                setattr(veri, sutun, request.json[sutun])
            else:
                return abort(500)
        db.session.commit()

        return veri.to_dict()

    @bp.route("/<int:id>", methods=["DELETE"])
    def sil(id: int):

        """

        :param id:
        :return:


        Veri tabanı modeli ile ilgili kayıt siler.
        """
        sorgu = select(veri_sinifi).where(veri_sinifi.id == id)
        veri = db.session.scalars(sorgu).one()

        db.session.delete(veri)
        db.session.commit()
        return {'silinen': veri.to_dict()}


    return bp
