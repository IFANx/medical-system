from flask import Blueprint, request
from sqlalchemy import func, or_
from app.database import db
from app.models import Hospital
from app.utils.to_json import hospital_to_json, hospitals_to_json


bp = Blueprint('hospitals', __name__, url_prefix='/hospitals')


'''/hospitals?q={query}&province={}&city={}&order={class}&page={uint}'''
@bp.route('', methods=['GET'])
def hospitals():
    if request.method == 'GET':
        q = request.args.get('q')
        province = request.args.get('province')
        city = request.args.get('city')
        order = request.args.get('order')
        hosclass = request.args.get('hosclass')
        page = request.args.get('page')

        h = db.session.query(Hospital)
        if q:
            h = h.filter(or_(Hospital.hos_name.like('%' + q + '%'), Hospital.introduction.like('%' + q + '%'),
                             Hospital.address.like('%' + q + '%')))
        if province:
            h = h.filter(Hospital.province == province)
        if city:
            h = h.filter(Hospital.city == city)
        if hosclass:
            h = h.filter(Hospital.hos_class == hosclass)
        if order == 'hosclass':
            h = h.order_by(Hospital.hos_class.desc())

        # 页面控制
        try:
            page = int(page)
            assert page > 0
        except:
            page = 1
        result = h.limit(20).offset(20 * (page - 1))

        return hospitals_to_json(result)


@bp.route('/<hid>', methods=['GET'])
def hospital(hid):
    if request.method == 'GET':
        h = Hospital.query.filter_by(hid=hid).first()
        return hospital_to_json(h)


@bp.route('/<hid>/<path>', methods=['GET'])
def hospital_info(hid, path):
    if request.method == 'GET':
        return 'hello %s' % hid
